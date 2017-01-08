package org.jlab.hallb.AutoLogEntry;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.sql.*;
import java.util.Date;
import java.lang.Thread;
import java.awt.image.*;
import javax.imageio.*;
import javax.swing.text.*;

import org.jlab.elog.LogEntry;

public class MakeLogEntry
{
  String LOGBOOKNAME="TLOG";

  String RUNDBSESSION="clashps";
  String RUNDBSERVER="clondb1:3306";
  String RUNDBTABLE="daq_clasrun";
  String RUNDBUSER="clasrun";
  String RUNDBPASSWD="";

  String SCREENSHOTDIR=System.getenv("HOME")+"/screenshots/";

  String USAGE="MakeLogEntry [-w windowId] [-m screenName]";
  String IMGPATH; // Path of image to submit to logbook

  JTextArea LOGTEXT = new JTextArea("Comments", 20, 40);
  JTextArea LOGTITLE = new JTextArea("Title", 20, 40);
  JTextPane STATUSTEXT = null;
  JPanel IMPANEL=new JPanel();
  JPanel BUTTONPANEL=null;
  JFrame FRAME;

  int IMGHEIGHT=200;
  int IMGWIDTH=300;

  public static void main( String[] args )
  {
    System.out.println("Running MakeLogEntry ...");
    try {
      MakeLogEntry obj = new MakeLogEntry();
      obj.run(args);
    }
    catch (Exception e) { e.printStackTrace(); }
  }

  public void run(String[] args)
  {
    try {
      // interpret arguments:
      String screenName=null;
      String windowId=null;
      for (int ii=0; ii<args.length; ii++)
      {
        if (ii+1 >= args.length)
          System.err.println("Invalid Arguments.\n"+USAGE);
        else
        {
          if      (args[ii].equals("-w")) windowId = args[++ii];
          else if (args[ii].equals("-m")) screenName = args[++ii];
          else System.err.println("Invalid Argument: >"+args[ii]+"<");
        }
      }
      // if window ID was given, take screenshot now:
      if (windowId != null)
      {
        IMGPATH = takeScreenshot(windowId, screenName);
        showScreenshot(IMGPATH);
      }
      // run the gui:
      makeGui();
    }
    catch (Exception e) { e.printStackTrace(); }
  }

  public String getWindowID()
  {
    // use xwininfo, and mouse left-click, to get X-window ID:
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
    // get current run number from database:
    int runNumber = 0;
    try { Class.forName("com.mysql.jdbc.Driver"); }
    catch (ClassNotFoundException e) { e.printStackTrace(); } 
    try {
      Connection conn = DriverManager.getConnection(
          "jdbc:mysql://"+RUNDBSERVER+"/"+RUNDBTABLE, RUNDBUSER, RUNDBPASSWD);
      ResultSet rs = conn.createStatement().executeQuery(
          "select runnumber from sessions where name=\""+RUNDBSESSION+"\" ;");
      while (rs.next()) runNumber=rs.getInt("runnumber");
    }
    catch (Exception e) { e.printStackTrace(); }
    return runNumber;
  }

  public String takeScreenshot(String winId, String medmName)
  {
    // use xwd and convert to take screenshot of X-window 
    String imgPath = null;
    try {
      String windowID = winId==null ? getWindowID() : winId;
      String stub = medmName; // command-line argument
      Date date = new Date();
      String timeStamp = String.format("%tY-%tm-%td_%tH-%tM-%tS",
          date,date,date,date,date,date);
      if (stub==null)
      {
        stub=System.getenv("HOST");
        if (stub.indexOf('.')>0)
          stub=stub.substring(0,stub.indexOf('.'));
      }
      imgPath = SCREENSHOTDIR+stub+"_"+timeStamp+".gif";
      System.out.println(imgPath);
      String[] cmd = {"/bin/sh", "-c", "xwd -id " + windowID + " | convert - " + imgPath };
      Runtime.getRuntime().exec(cmd);
    }
    catch (Exception e) { e.printStackTrace(); java.lang.System.exit(0); }
    return imgPath;
  }

  public void showScreenshot(String filename)
  {
    // try/wait for file to register, and sleep before reading it:
    File file=null;
    BufferedImage imbuff = null;
    try {
      int count=0;
      boolean goodFile=false;
      for (count=0; count<50; count++) {
        file=new File(filename);
        if (file.isFile()) { goodFile=true; break; }
        sleep(200);
      }
      if (!goodFile) 
      {
        System.err.println("File DNE:  "+filename);
        return;
      }
      if (count>5) System.err.println("WAITCOUNT:  "+count);
      sleep(500);
      imbuff=ImageIO.read(new File(filename));
    }
    catch (IOException e) { e.printStackTrace(); }
    Image image = getScaledImage(imbuff);
    ImageIcon imicon=new ImageIcon(image);
    IMPANEL.removeAll();
    IMPANEL.updateUI();
    IMPANEL.add(new JLabel(imicon));
  }

  public Image getScaledImage(BufferedImage imbuff)
  {
    // scale for snapshot, preserving the aspect ratio:
    float height=imbuff.getHeight();
    float width=imbuff.getWidth();
    float aspectRatio=height/width;
    float ASPECTRATIO=(float)IMGHEIGHT/IMGWIDTH;
    if (aspectRatio > ASPECTRATIO) {
      height=IMGHEIGHT;
      width=IMGWIDTH/aspectRatio*ASPECTRATIO;
    }
    else {
      width=IMGWIDTH;
      height=IMGHEIGHT*aspectRatio/ASPECTRATIO;
    }
    return imbuff.getScaledInstance((int)width,(int)height,Image.SCALE_SMOOTH);
  }

  public JTextPane makeTextPane(String text,Color color)
  {
    // don't remember why JTextPane instead of just JTextArea
    JTextPane jtp = new JTextPane();
    StyledDocument doc = jtp.getStyledDocument();
    Style style = jtp.addStyle("a",null);
    StyleConstants.setForeground(style,color);
    try { doc.insertString(doc.getLength(),text,style); }
    catch (BadLocationException e){}
    jtp.setVisible(true);
    jtp.setEditable(false);
    jtp.setFont(new Font("Diaglog.plain",0,15));
    jtp.setOpaque(false);
    return jtp;
  }

  public void makeGui()
  {
    FRAME = new JFrame("Hall B Logbook Entry");
    FRAME.getContentPane().setBackground(Color.LIGHT_GRAY);
    FRAME.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    // for screenshot:
    IMPANEL.setPreferredSize(new Dimension(IMGWIDTH,IMGHEIGHT));

    // log title instructions:
    JTextPane logTitleInst = makeTextPane("Enter Log Title:",Color.DARK_GRAY);
    logTitleInst.setPreferredSize(new Dimension(200, 20));

    // log title entry:
    LOGTITLE.setText("Run #"+Integer.toString(getRunNumber())+":  ");
    LOGTITLE.setVisible(true);
    LOGTITLE.setEditable(true);
    LOGTITLE.setForeground(Color.BLUE);
    LOGTITLE.setFont(new Font("Diaglog.plain",0,15));
    LOGTITLE.setPreferredSize(new Dimension(400, 20));
    LOGTITLE.setMaximumSize(new Dimension(1000, 20));

    // log text instructions:
    JTextPane logTextInst = makeTextPane("Enter Log Content:",Color.DARK_GRAY);
    logTextInst.setPreferredSize(new Dimension(400, 20));

    STATUSTEXT = makeTextPane("",Color.RED);
    STATUSTEXT.setPreferredSize(new Dimension(400,25));

    // log text entry:
    LOGTEXT.setLineWrap(true);
    LOGTEXT.setWrapStyleWord(true);
    LOGTEXT.setMinimumSize(new Dimension(10, 10));
    LOGTEXT.setForeground(Color.BLUE);
    LOGTEXT.setFont(new Font("Dialog.plain", 0, 15));
    scrollablePanel sp = new scrollablePanel();
    BoxLayout layout = new BoxLayout(sp, BoxLayout.Y_AXIS);
    sp.setLayout(layout);
    sp.add(LOGTEXT);
    sp.add(Box.createRigidArea(new Dimension(0, 10)));
    JScrollPane jsp = new JScrollPane(sp);
    jsp.getVerticalScrollBar().setUnitIncrement(16);
    jsp.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
    jsp.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
    jsp.setPreferredSize(new Dimension(500,200));

    // buttons:
    JButton butSubmit = new JButton();
    butSubmit.setText("Submit");
    butSubmit.addActionListener(new submitAction());
    JButton butScreenshot = new JButton();
    butScreenshot.setText("Screenshot");
    butScreenshot.addActionListener(new screenshotAction());
    JButton butCancel = new JButton();
    butCancel.setText("Exit");
    butCancel.addActionListener(new exitAction());
    BUTTONPANEL = new JPanel();
    BUTTONPANEL.add(STATUSTEXT);
    BUTTONPANEL.add(butScreenshot);
    BUTTONPANEL.add(butSubmit);
    BUTTONPANEL.add(butCancel);

    JPanel titlePanel = new JPanel();
    titlePanel.setLayout(new FlowLayout(FlowLayout.LEADING));
    titlePanel.setPreferredSize(new Dimension(200, 70));
    titlePanel.add(logTitleInst);
    titlePanel.add(LOGTITLE);

    JPanel topPanel = new JPanel();
    topPanel.setLayout(new BoxLayout(topPanel,BoxLayout.PAGE_AXIS));
    topPanel.setPreferredSize(new Dimension(200, 80));
    topPanel.add(titlePanel);
    topPanel.add(logTextInst);

    titlePanel.setOpaque(false);
    jsp.setOpaque(false);
    BUTTONPANEL.setOpaque(false);
    topPanel.setOpaque(false);
    IMPANEL.setOpaque(false);

    FRAME.add(jsp, BorderLayout.CENTER);
    FRAME.add(BUTTONPANEL, "South");
    FRAME.add(topPanel, "North");
    FRAME.add(IMPANEL,"East");
    FRAME.pack();
    FRAME.setVisible(true);
  }

  public void forceUpdateStatusPane()
  {
    // at least one of these is important:
    STATUSTEXT.update(STATUSTEXT.getGraphics());
    STATUSTEXT.updateUI();
    STATUSTEXT.repaint();
    BUTTONPANEL.update(BUTTONPANEL.getGraphics());
    BUTTONPANEL.updateUI();
    BUTTONPANEL.repaint();
    FRAME.update(FRAME.getGraphics());
    FRAME.revalidate();
    FRAME.repaint();
  }

  public void updateStatusPane(String text, Color color,int size)
  {
    STATUSTEXT.removeAll();
    StyledDocument doc=STATUSTEXT.getStyledDocument();
    try { doc.remove(0,doc.getLength()); }
    catch (BadLocationException e){}
    doc.removeStyle("a");
    Style style = STATUSTEXT.addStyle("a",null);
    StyleConstants.setForeground(style,color);
    StyleConstants.setBold(style,true);
    if (size<=0) size=16;
    STATUSTEXT.setFont(new Font("Dialog.plain",0,size));
    try { doc.insertString(doc.getLength(),text,style); }
    catch (BadLocationException e){}
    forceUpdateStatusPane();
  }
  public void updateStatusPane(String text, Color color) { updateStatusPane(text,color,-1); }

  public void sleep(int time)
  {
    try { Thread.sleep(time); }
    catch (InterruptedException e) { e.printStackTrace(); }
  }

  public void submitElog()
  {
    LogEntry entry = new LogEntry("", LOGBOOKNAME);
    //entry.setEmailNotify("rafopar@jlab.org");
    try {
      entry.addAttachment(IMGPATH,"Snapshot of "+IMGPATH);
      entry.setTitle(LOGTITLE.getText());
      entry.setBody(LOGTEXT.getText());
      long logNumber = entry.submitNow();
      //entry.submit();
      //System.out.println(entry.getXML());
      System.out.println("Log #" + logNumber+" Submitted.");
      updateStatusPane("Log #"+logNumber+" Submitted.",Color.RED);
    }
    catch (Exception e) { 
      System.err.println("Error Submitting To Logbook:\n"+e.getMessage());
      updateStatusPane("Error Submitting To Logbook.",Color.RED);
    }
  }

  class screenshotAction implements ActionListener
  {
    public void actionPerformed (ActionEvent e) {
      updateStatusPane("Left-Click in a Window for Screenshot ...",Color.RED);
      IMGPATH=takeScreenshot(null,null);
      String imgpath=IMGPATH;
      String home=System.getenv("HOME");
      if (imgpath.indexOf(home)==0)
        imgpath="~"+imgpath.substring(home.length(),imgpath.length());
      showScreenshot(IMGPATH);
      updateStatusPane(imgpath,Color.BLACK,11);
    }
  }
  class submitAction implements ActionListener
  {
    public void actionPerformed (ActionEvent e) { submitElog(); }
  }
  class exitAction implements ActionListener
  {
    public void actionPerformed (ActionEvent e) { FRAME.dispose(); }
  }

  private static class scrollablePanel extends JPanel implements Scrollable
  {
    public int getScrollableUnitIncrement(Rectangle visibleRect, int orientation, int direction)  { return 16; }
    public int getScrollableBlockIncrement(Rectangle visibleRect, int orientation, int direction) { return 16; }
    public Dimension getPreferredScrollableViewportSize() { return super.getPreferredSize(); }
    public boolean getScrollableTracksViewportWidth()  { return true; }
    public boolean getScrollableTracksViewportHeight() { return false; }
  }

}
