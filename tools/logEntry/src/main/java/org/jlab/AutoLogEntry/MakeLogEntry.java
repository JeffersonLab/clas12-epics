package org.jlab.AutoLogEntry;

import java.awt.*;
import java.awt.event.*;
//import javax.*;
import javax.swing.*;

import org.jlab.elog.LogEntry;
import java.awt.Window;
import java.awt.Frame ;

import java.io.*;
import java.sql.*;

import java.util.Date;

public class MakeLogEntry
{
    String winid;        // Window ID, that we need to get an image from
    String medm_name;    // The name of MEDM (.adl) file
    String img_path;     // Path of the Image, that will be submited to logbook
    String file_name = "NO FILENAME";           // An .adl file nemae without ".adl", e.g. tagger_dump_lamp or hiv_alarm etc
    String fit_parameters = "";
    String AdditionalText = "";
    String PV_list = ""; // List of Process Variables
    String medm_dir = "";
    String elog_Title = "";
    JTextArea jta2 = new JTextArea("Comments", 20, 40);  // Text are where user can type comments
    JFrame frame;
    String comments_to_submit;     // Comments in addition to the 
    long lognumber;
    int run_number = -1;
    JRadioButton rb_important;    

    public static void main( String[] args )
    {
        System.err.println("Running MakeLogEntry ...");
        try {
            MakeLogEntry obj = new MakeLogEntry();
            obj.main_run(args);
        }
        catch( Exception e)
        {
            e.printStackTrace();
        }
    }

    public void main_run(String[] args) throws Exception
    {
        try{
            Init();
            winid = args[0];
            medm_name = args[1];
            System.out.println(winid);
            System.out.println(medm_name);

            img_path = getImgPath(winid, medm_name);
            System.out.println("Img Full path = " + img_path);

            PV_list = PV_list + getPVs("chan");
            PV_list = PV_list + getPVs("rdbk");
            PV_list = PV_list + getPVs("ydata");

            run_number = getRunNumber();
            elog_Title = "Snapshot of " + file_name + " : Run " + run_number;

            addComments();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }

    }

    public void Init()
    {
        medm_dir = System.getenv("EPICS_DISPLAY_PATH");
        System.out.println("EPICS_DISPLAY_PATH is " + medm_dir);
    }

    public String getImgPath( String winid, String medm_name)
    {
        String IMG_path = null;
        try{
            Process p;
            BufferedReader stdInput;
            
            String[] asdf = {"xwininfo"};
            p = Runtime.getRuntime().exec(asdf);
            stdInput = new BufferedReader(new InputStreamReader( p.getInputStream() ));
            System.err.println(stdInput);
            

            String[] file_name_command = {"/bin/sh", "-c", "echo " + medm_name + " | sed -e s/.adl//"};
            String time_stamp = getTimeStamp(); // time in a format YYYY_MM_DD_HH_mm_SS (year month day hour min sec)

            p = Runtime.getRuntime().exec(file_name_command);
            stdInput = new BufferedReader(new InputStreamReader( p.getInputStream() ));
            file_name = stdInput.readLine();

            p = Runtime.getRuntime().exec("pwd" );
            stdInput = new BufferedReader(new InputStreamReader( p.getInputStream() ));
            String cur_dir = stdInput.readLine();

            String home_dir = System.getenv("HOME");
            String snapshot_dir = home_dir+"/screenshots";
            String[] cmd_convert = {"/bin/sh", "-c", "xwd -id " + winid + " | convert - " + snapshot_dir + "/" + file_name+"_"+time_stamp+".gif"};
            p = Runtime.getRuntime().exec(cmd_convert );

            IMG_path = snapshot_dir+"/"+file_name+"_"+time_stamp+".gif";
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }

        return IMG_path;
    }

    public void addComments()
    {
        frame = new JFrame("Additional Comments");
        //frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JTextArea jta1 = new JTextArea("Please add additional information below");
        jta1.setVisible(true);
        jta1.setEditable(false);
        Font f2 = new Font("Dialog.plain", 0, 25);
        jta1.setFont(f2);
        jta1.setForeground(Color.BLUE);

        Font f_comment = new Font("Dialog.plain", 0, 20);
        jta2.setLineWrap(true);
        jta2.setWrapStyleWord(true);
        jta2.setMinimumSize(new Dimension(10, 10));
        jta2.setFont(f_comment);

        ScrollablePanel innerContainer = new ScrollablePanel();
        BoxLayout layout = new BoxLayout(innerContainer, BoxLayout.Y_AXIS);
        innerContainer.setLayout(layout);

        innerContainer.add(jta1);
        innerContainer.add(Box.createRigidArea(new Dimension(0, 10)));

        innerContainer.add(jta2);
        innerContainer.add(Box.createRigidArea(new Dimension(0, 10)));

        JScrollPane scrollPane = new JScrollPane(innerContainer);

        scrollPane.getVerticalScrollBar().setUnitIncrement(16);
        scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
        scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);

        frame.getContentPane().add(scrollPane, BorderLayout.CENTER);


        // ================= A radiobutton "Needs attention" ===================
        rb_important = new JRadioButton("Needs special attention?");

        // ============== The Submit button =================

        JButton but_submit = new JButton();
        but_submit.setText("Submit");
        but_submit.addActionListener(new Action());

        JPanel down_panel = new JPanel();
        frame.getContentPane().add(down_panel, "South");
        //down_panel.add(rb_important);
        down_panel.add(but_submit);

        frame.pack();
        frame.setVisible(true);
    }

    public static String getTimeStamp()
    {
        Date date = new Date();

        String str_year = String.format("%tY", date);
        String str_month = String.format("%tm", date);
        String str_day = String.format("%td", date);
        String str_hour = String.format("%tH", date);
        String str_min = String.format("%tM", date);
        String str_sec = String.format("%tS", date);

        String time_stamp = str_year+"_"+str_month+"_"+str_day+"_"+str_hour+"_"+str_min+"_"+str_sec;
        return time_stamp;
    }


    public void SubmitElog()
    {
        System.err.println("NOT SUBMITTING ELOG");
/*
        //LogEntry entry = new LogEntry("", "TLOG");
        LogEntry entry = new LogEntry("", "HBLOG");
        //entry.setEmailNotify("rafopar@jlab.org");

        try {
            entry.addAttachment( img_path, "Snapshot of " + file_name + "window");
            System.out.println("The title is: " + elog_Title);
            entry.setTitle(elog_Title);	
            String Setaratition_line = "\n ================= PVs ==================== \n";
            entry.setBody("[figure:1] \n" + comments_to_submit + Setaratition_line + AdditionalText + "\n \n" + PV_list);

            System.out.println("The PV list is " + PV_list);

            if( rb_important.isSelected() ) // Checks whether this entry needs special attention
            {
                entry.setSticky(true);
                System.out.println("Needs Special Attention");
            }

            lognumber = entry.submitNow();
            //entry.submit();
            System.out.println("Entry was submited under the lognumber " + lognumber);
            //System.out.println(entry.getXML());

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
*/
    }


    // This method return list of values PVs corresponding to a particular keyword e.g chan, rdbg ydata
    public String getPVs(String keyword)
    {
        Process p;
        BufferedReader stdInput;
        BufferedReader stdError;
        String s = null;
        String PV_sub_list = "";

        try{
            String[] command = {"/bin/sh", "-c", "caget `cat " + medm_dir+"/"+medm_name + " | grep " + keyword + "= | cut -d '=' -f2 | sort | sed -e s/" + "\\" + "\"// | sed -e s/" + "\\" + "\"//`"};
            p = Runtime.getRuntime().exec(command);
            stdInput = new BufferedReader(new InputStreamReader( p.getInputStream() ));

            String line = null;

            while ((line = stdInput.readLine())!= null)
            {
                System.out.println("line = " + line);
                PV_sub_list = PV_sub_list +"\n" + line;
            }

        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return PV_sub_list;
    }

//    private String rundbConn="jdbc:mysql://clondb1:3306/daq_clasrun";
//    private String rundbUser="clasrun";
//    private String rundbSessionName="clashps";

    // This method should return current run number. 
    //It will take the information from the "daq_clasdev" databas on clondb1 machine from the table sessions
    public int getRunNumber()
    {
        int cur_runnumber = 0;
        try{
            Class.forName("com.mysql.jdbc.Driver");
        }catch (ClassNotFoundException e) {
            e.printStackTrace();
        } 

        try{
            BufferedReader stdInput;
            //Connection conn = DriverManager.getConnection("jdbc:mysql://clondb1:3306/daq_clasdev", "clasrun", "");
            Connection conn = DriverManager.getConnection("jdbc:mysql://clondb1:3306/daq_clasrun", "clasrun", "");
            Statement stmt = conn.createStatement();
            String query = "select runnumber from sessions where name=\"clashps\" ;" ;

            ResultSet rs = stmt.executeQuery(query) ;

            while( rs.next() )
            {
                cur_runnumber =  rs.getInt("runnumber");
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }

        return cur_runnumber;
    }


    class Action implements ActionListener
    {
        public void actionPerformed (ActionEvent e)
        {
            comments_to_submit = jta2.getText();

            comments_to_submit = comments_to_submit + fit_parameters;

            System.out.println(comments_to_submit);

            SubmitElog();
            //frame.setVisible(false);
            frame.dispose();
            //System.exit(0);
        }
    }


    public void AddAdditionalText(String a)
    {
        AdditionalText = AdditionalText + a;
        System.out.println("Additional text is \n" + a);
    }


    private static class ScrollablePanel extends JPanel implements Scrollable{
        public Dimension getPreferredScrollableViewportSize() {
            return super.getPreferredSize();
        }

        public int getScrollableUnitIncrement(Rectangle visibleRect, int orientation, int direction) {
            return 16;
        }

        public int getScrollableBlockIncrement(Rectangle visibleRect, int orientation, int direction) {
            return 16;
        }

        public boolean getScrollableTracksViewportWidth() {
            return true;
        }

        public boolean getScrollableTracksViewportHeight() {
            return false;
        }
    }

}
