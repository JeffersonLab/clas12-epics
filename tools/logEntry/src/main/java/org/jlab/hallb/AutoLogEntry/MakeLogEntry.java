package org.jlab.hallb.AutoLogEntry;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.awt.Window;
import java.awt.Frame ;
import java.io.*;
import java.sql.*;
import java.util.Date;

import org.jlab.elog.LogEntry;

public class MakeLogEntry
{
    String LOGBOOKNAME="TLOG";

    String RUNDBSERVER="clondb1:3306";
    String RUNDBTABLE="daq_clasrun";
    String RUNDBUSER="clasrun";
    String RUNDBPASSWD="";

    String WINID=null;      // Window ID, that we need to get an image from
    String MEDMNAME=null; // The name of MEDM (.adl) file
    String IMGPATH;       // Path of the Image, that will be submited to logbook
    String FILENAME = "NO FILENAME";           // An .adl file nemae without ".adl", e.g. tagger_dump_lamp or hiv_alarm etc
    JTextArea LOGTEXT = new JTextArea("Comments", 20, 40);  // Text are where user can type comments
    JTextArea LOGTITLE = new JTextArea("Title", 20, 40);  // Text are where user can type comments
    JFrame FRAME;

    public static void main( String[] args )
    {
        System.err.println("Running MakeLogEntry ...");
        try {
          MakeLogEntry obj = new MakeLogEntry();
          obj.run(args);
        }
        catch (Exception e) { e.printStackTrace(); }
    }

    public void run(String[] args)
    {
          try {
            if (args.length>0) WINID = args[0];
            if (args.length>1) MEDMNAME = args[1];
            IMGPATH = getImgPath(WINID, MEDMNAME);
            getUserInput();
          }
          catch (Exception e) { e.printStackTrace(); }
    }
    
    public static String getTimeStamp()
    {
        Date date = new Date();
        String year = String.format("%tY", date);
        String month = String.format("%tm", date);
        String day = String.format("%td", date);
        String hour = String.format("%tH", date);
        String min = String.format("%tM", date);
        String sec = String.format("%tS", date);
        return year+"_"+month+"_"+day+"_"+hour+"_"+min+"_"+sec;
    }

    public String getWindowID()
    {
      String windowID=null;
      try {
        String[] cmd = {"/usr/bin/xwininfo"};
        Process proc = Runtime.getRuntime().exec(cmd);
        proc.waitFor();
        InputStreamReader isr = new InputStreamReader(proc.getInputStream());
        BufferedReader br = new BufferedReader(new InputStreamReader(proc.getInputStream()));
        String line;
        while ((line=br.readLine()) != null) {
          // here's the parsing of xwininfo output:
          if (line.startsWith("xwininfo: Window id: ")) {
            String[] parts=line.split(" ");
            windowID=parts[3];
            break;
          }
        }
        br.close();
      }
      catch (Exception e) { e.printStackTrace(); }
      return windowID;
    }
    
    public int getRunNumber()
    {
        int runNumber = 0;
        try { Class.forName("com.mysql.jdbc.Driver"); }
        catch (ClassNotFoundException e) { e.printStackTrace(); } 
        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://"+RUNDBSERVER+"/"+RUNDBTABLE, RUNDBUSER, RUNDBPASSWD);
            ResultSet rs = conn.createStatement().executeQuery("select runnumber from sessions where name=\"clashps\" ;");
            while (rs.next()) runNumber=rs.getInt("runnumber");
        }
        catch (Exception e) { e.printStackTrace(); }
        return runNumber;
    }

    public String getImgPath(String winid, String medmName)
    {
        String imgPath = null;
        try {
            String windowID = getWindowID();
            String stub = medmName; // command-line argument
            String dir = System.getenv("HOME")+"/screenshots/";
            String timeStamp = getTimeStamp();
            imgPath = dir+stub+"_"+timeStamp+".gif";
            System.err.println(imgPath);
            String[] cmd = {"/bin/sh", "-c", "xwd -id " + windowID + " | convert - " + imgPath };
            Runtime.getRuntime().exec(cmd);
        }
        catch (Exception e) { e.printStackTrace(); java.lang.System.exit(0); }
        return imgPath;
    }

    public void getUserInput()
    {
        FRAME = new JFrame("Hall B Logbook Entry");
        FRAME.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // log title instructions:
        JTextArea logTitleInst = new JTextArea("Enter Log Title:");
        logTitleInst.setVisible(true);
        logTitleInst.setEditable(false);
        logTitleInst.setFont(new Font("Diaglog.plain",0,20));
        
        // log title entry:
        LOGTITLE.setText("Run #"+Integer.toString(getRunNumber())+":  ");
        LOGTITLE.setVisible(true);
        LOGTITLE.setEditable(true);
        LOGTITLE.setForeground(Color.BLUE);
        LOGTITLE.setFont(new Font("Diaglog.plain",0,20));
        LOGTITLE.setMaximumSize(new Dimension(10, 50));

        // log text instructions:
        JTextArea logTextInst = new JTextArea("Please add additional information below:");
        logTextInst.setVisible(true);
        logTextInst.setEditable(false);
        logTextInst.setFont(new Font("Dialog.plain", 0, 20));

        // log text entry:
        LOGTEXT.setLineWrap(true);
        LOGTEXT.setWrapStyleWord(true);
        LOGTEXT.setMinimumSize(new Dimension(10, 10));
        LOGTEXT.setForeground(Color.BLUE);
        LOGTEXT.setFont(new Font("Dialog.plain", 0, 20));
        scrollablePanel sp = new scrollablePanel();
        BoxLayout layout = new BoxLayout(sp, BoxLayout.Y_AXIS);
        sp.setLayout(layout);
        sp.add(LOGTEXT);
        sp.add(Box.createRigidArea(new Dimension(0, 10)));
        JScrollPane jsp = new JScrollPane(sp);
        jsp.getVerticalScrollBar().setUnitIncrement(16);
        jsp.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
        jsp.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
        FRAME.getContentPane().add(jsp, BorderLayout.CENTER);

        // buttons:
        JButton butSubmit = new JButton();
        butSubmit.setText("Submit To Logbook");
        butSubmit.addActionListener(new submitAction());
        JButton butScreenshot = new JButton();
        butScreenshot.setText("Add Screenshot");
        //butScreenshot.addActionListener(new screenshotAction());
        JPanel buttonPanel = new JPanel();
        FRAME.getContentPane().add(buttonPanel, "South");
        buttonPanel.add(butScreenshot);
        buttonPanel.add(butSubmit);

        JPanel titlePanel = new JPanel();
        titlePanel.add(logTitleInst);
        titlePanel.add(LOGTITLE);
        //titlePanel.setMaximumSize(new Dimension(10, 20));
        
        JPanel topPanel = new JPanel();
        //topPanel.setLayout(new GridLayout(2,1));
        topPanel.add(titlePanel);
        topPanel.add(logTextInst);
        topPanel.setMaximumSize(new Dimension(10, 50));

        JPanel instructPanel = new JPanel();
        instructPanel.add(logTextInst);

        FRAME.getContentPane().add(instructPanel, "North");
        //FRAME.getContentPane().add(topPanel, "North");

        FRAME.pack();
        FRAME.setVisible(true);
    }


    public void submitElog()
    {
        System.err.println("NOT SUBMITTING ELOG");
/*
        LogEntry entry = new LogEntry("", LOGBOOKNAME);
        //entry.setEmailNotify("rafopar@jlab.org");
        try {
            entry.addAttachment(IMGPATH,"Snapshot of "+IMGPATH);
            entry.setTitle(LOGTITLE.getText());
            entry.setBody(LOGTEXT.getText());
            long logNumber = entry.submitNow();
            System.out.println("Log Submitted as Entry #" + logNumber);
            //entry.submit();
            //System.out.println(entry.getXML());
        }
        catch (Exception e) { System.out.println(e.getMessage()); }
*/
    }

    class submitAction implements ActionListener
    {
        public void actionPerformed (ActionEvent e)
        {
            submitElog();
            FRAME.dispose();
        }
    }

    /*
    class screenshotAction implements ActionListener
    {
        public void actionPerformed (ActionEvent e)
        {
            TakeScreenshot();
            FRAME.dispose();
        }
    }
    */

    private static class scrollablePanel extends JPanel implements Scrollable
    {
        public int getScrollableUnitIncrement(Rectangle visibleRect, int orientation, int direction)  { return 16; }
        public int getScrollableBlockIncrement(Rectangle visibleRect, int orientation, int direction) { return 16; }
        public Dimension getPreferredScrollableViewportSize() { return super.getPreferredSize(); }
        public boolean getScrollableTracksViewportWidth()  { return true; }
        public boolean getScrollableTracksViewportHeight() { return false; }
    }

}
