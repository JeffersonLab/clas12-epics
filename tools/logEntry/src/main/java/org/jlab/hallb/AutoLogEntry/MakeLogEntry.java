package org.jlab.hallb.AutoLogEntry;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.Set;
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
import javax.swing.border.*;

import org.jlab.elog.LogEntry;

public class MakeLogEntry
{
  String LOGBOOKNAME="HBLOG";

  String[] LOGBOOKS = {"HBLOG","HBDC","HBECAL","HBMVT","HBSVT","HBTOF","HBSOLENOID","HBTORUS","HBCONTROLS","FT","HTCC","LTCC","RICH","CLAS12ANA","TLOG"};

//  String RUNDBSESSION=System.getenv("SESSION");
//  String RUNDBEXPID=System.getenv("EXPID");
//  String RUNDBTABLE="daq_"+RUNDBEXPID;
//  String RUNDBUSER=RUNDBEXPID;
 
  // kpp settings:
  String RUNDBSESSION="clasprod";
  String RUNDBTABLE="daq_clasrun";

  // hps settings:
  //String RUNDBSESSION="clashps";
  //String RUNDBTABLE="daq_clasrun";
  
  final String RUNDBHOST=System.getenv("MYSQL_HOST");
  final String RUNDBPORT="3306";

  final String RUNDBUSER="clasrun"; // $EXPID?
  final String RUNDBPASSWD="";

  final String SCREENSHOTDIR=System.getenv("HOME")+"/screenshots/";
  final String USAGE="MakeLogEntry [-w windowId] [-m screenName] [-l logBookName] [-s runDbSession]";
  String IMGPATH = null; // Path of image to submit to logbook

  JTextArea LOGTEXT = new JTextArea("Enter Comments Here", 20, 40);
  JTextArea LOGTITLE = new JTextArea("Title", 20, 40);
  JTextPane STATUSTEXT = null;
  JPanel IMPANEL=new JPanel();
  JFrame FRAME;
    
  JComboBox<String> LOGBOOKCHOICE=new JComboBox<>(LOGBOOKS);

  //CheckComboBox LOGBOOKCHOICE;

  final boolean DEBUG=false;

  String stockTitle="";

  boolean DOTABS=true;
  ArrayList<JPanel> IMPANELS = new ArrayList<JPanel>();
  ArrayList<String> IMPATHS = new ArrayList<String>();
  JTabbedPane IMTABS;
	JButton ADDTABBTN = new JButton("+");

  int IMGHEIGHT = 200;
  int IMGWIDTH = 300;

  public void MakeLogEntry() {

      //Set dog=new LinkedHashSet();
      //for (String ss : LOGBOOKS) dog.add(ss);
      //LOGBOOKCHOICE=new CheckComboBox(dog);
  }


  public static void main( String[] args )
  {
    //System.out.println("Running MakeLogEntry ...");
    try {
      MakeLogEntry obj = new MakeLogEntry();
      obj.run(args);
    }
    catch (Exception e) { e.printStackTrace(); }
  }

  public void run(String[] args)
  {
      System.out.println(SCREENSHOTDIR);
      File fff= new File(SCREENSHOTDIR);
      fff.mkdir();

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
          else if (args[ii].equals("-l")) {
              LOGBOOKNAME = args[++ii];
              boolean found=false;
              for (String ss : LOGBOOKS)
              {
                  if (LOGBOOKNAME.equals(ss)) {
                      found=true;
                      break;
                  }
                  
              }
              if (!found) {
                  System.err.println("Invalid logbook name: "+LOGBOOKNAME);
                  LOGBOOKNAME="HBLOG";
              }
          }
          else if (args[ii].equals("-s")) RUNDBSESSION = args[++ii];
          else if (args[ii].equals("-t")) DOTABS = Boolean.parseBoolean(args[++ii]);
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
      String host = "jdbc:mysql://"+RUNDBHOST+":"+RUNDBPORT+"/"+RUNDBTABLE;
      String query = "select runnumber from sessions where name=\""+RUNDBSESSION+"\" ;";
      Connection conn = DriverManager.getConnection(host,RUNDBUSER, RUNDBPASSWD);
      ResultSet rs = conn.createStatement().executeQuery(query);
      while (rs.next()) runNumber=rs.getInt("runnumber");
    }
    catch (Exception e) { e.printStackTrace(); }
    return runNumber;
  }

  public String takeScreenshot(String winId, String medmName)
  {
    String imgPath = null;
    try {
      String stub = medmName; // command-line argument
      Date date = new Date();
      String timeStamp = String.format("%tY%tm%td_%tH%tM%tS",
          date,date,date,date,date,date);
      if (stub==null)
      {
        stub=System.getenv("HOST");
        if (stub.indexOf('.')>0)
          stub=stub.substring(0,stub.indexOf('.'));
      }
      imgPath = SCREENSHOTDIR+stub+"_"+timeStamp+".gif";
      if (DEBUG) System.out.println(imgPath);
      if (winId==null) 
      {
        String[] cmd={"import",imgPath};
        Runtime.getRuntime().exec(cmd);
      }
      else
      {
        String[] cmd = {"xwd"," -id "+getWindowID()+" | convert - "+imgPath};
        Runtime.getRuntime().exec(cmd);
      }
    }
    catch (Exception e) { e.printStackTrace(); java.lang.System.exit(0); }
    return imgPath;
  }

  public BufferedImage readScreenshot(String filename)
  {
    // try/wait for file to register, and sleep before reading it.
    // all these loops, sleeps, tests were found to be important for reliability
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
        updateStatusPane("Error Displaying Screenshot.  Try Again.",Color.RED);
        return null;
      }
      if (count>10) System.err.println("MakeLogEntry.java:  WAITCOUNT1:  "+count);
      sleep(500);
      for (count=0; count<50; count++) {
        imbuff=ImageIO.read(file);
        if (imbuff==null) sleep(200);
        else break;
      }
      if (count>10) System.err.println("MakeLogEntry.java:  WAITCOUNT2:  "+count);
      if (imbuff==null) 
      {
        System.err.println("Error Displaying Screenshot.");
        updateStatusPane("Error Displaying Screenshot.  Try Again.",Color.RED);
      }
    }
    catch (IOException e) { e.printStackTrace(); }
    return imbuff;
  }

  public void showScreenshot(String filename)
  {
    IMPANEL.removeAll();
    if (filename != null)
    {
      BufferedImage imbuff = readScreenshot(filename);
      Image image = getScaledImage(imbuff);
      ImageIcon imicon=new ImageIcon(image);
      if (DOTABS)
      { 
        final int ii=IMTABS.getSelectedIndex();
        if (ii>=0 && ii<IMPANELS.size()) {
          if (DEBUG) System.out.println("showScreenshot:  "+ii);
          IMPATHS.set(ii,filename);
          IMPANELS.get(ii).removeAll();
          IMPANELS.get(ii).add(new JLabel(imicon));
        }
      }
      else IMPANEL.add(new JLabel(imicon));
    }
    for (JPanel jp : IMPANELS) jp.updateUI();
    IMPANEL.updateUI();
  }

  public Image getScaledImage(BufferedImage imbuff)
  {
    // scale for snapshot, preserving the aspect ratio:
    //IMGHEIGHT=IMPANEL.getHeight();
    //IMGWIDTH=IMPANEL.getWidth();
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
    // don't remember why JTextPane instead of just JTextArea (fg/bg color, bold font ...)
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

  public void initLogTitle()
  {
    LOGTITLE.setText("Run #"+Integer.toString(getRunNumber())+":  ");
    LOGTITLE.updateUI();
    stockTitle=LOGTITLE.getText();
  }
  
  public void initLogComments()
  {
    LOGTEXT.setText("Enter Comments Here");
    LOGTEXT.updateUI();
  }

  public void makeGui()
  {
    // screenshot panel:
    IMPANEL.setPreferredSize(new Dimension(IMGWIDTH,IMGHEIGHT));
    IMPANEL.setBorder(BorderFactory.createBevelBorder(BevelBorder.LOWERED));
    IMPANEL.setOpaque(false);
    
    // status line:
    STATUSTEXT = makeTextPane("",Color.RED);
    STATUSTEXT.setPreferredSize(new Dimension(500,25));

    // log title entry:
    initLogTitle();
    LOGTITLE.setVisible(true);
    LOGTITLE.setEditable(true);
    LOGTITLE.setForeground(Color.BLUE);
    LOGTITLE.setFont(new Font("Dialog.plain",0,15));
    LOGTITLE.setPreferredSize(new Dimension(400, 15));
    LOGTITLE.setBorder(BorderFactory.createBevelBorder(BevelBorder.LOWERED));

    // log text entry:
    LOGTEXT.setLineWrap(true);
    LOGTEXT.setWrapStyleWord(true);
    LOGTEXT.setMinimumSize(new Dimension(10, 10));
    LOGTEXT.setForeground(Color.BLUE);
    LOGTEXT.setFont(new Font("Dialog.plain", 0, 15));

    // log text entry panel:
    scrollablePanel sp = new scrollablePanel();
    sp.setLayout(new BoxLayout(sp, BoxLayout.Y_AXIS));
    sp.add(LOGTEXT);
    sp.add(Box.createRigidArea(new Dimension(0, 10)));
    JScrollPane jsp = new JScrollPane(sp);
    jsp.getVerticalScrollBar().setUnitIncrement(16);
    jsp.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
    jsp.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
    jsp.setPreferredSize(new Dimension(300,200));
    jsp.setBorder(BorderFactory.createBevelBorder(BevelBorder.LOWERED));
    jsp.setOpaque(false);

    // buttons:
    JButton butSubmit = new JButton();
    butSubmit.setText("Submit");
    butSubmit.addActionListener(new submitAction());
    JButton butScreenshot = new JButton();
    butScreenshot.setText("Screenshot");
    butScreenshot.addActionListener(new screenshotAction());
    JButton butClear = new JButton();
    butClear.setText("Reset");
    butClear.addActionListener(new clearAction());
    JButton butCancel = new JButton();
    butCancel.setText("Exit");
    butCancel.addActionListener(new exitAction());

    Border lbd=BorderFactory.createLineBorder(Color.GRAY);
    
    LOGBOOKCHOICE.setSelectedItem(LOGBOOKNAME);

    // button panel:
    JPanel buttonPanel = new JPanel();
    buttonPanel.setOpaque(false);
    if (!DOTABS) buttonPanel.add(butScreenshot);
    buttonPanel.add(butSubmit);
    buttonPanel.add(butClear);
    //buttonPanel.add(butCancel);
    buttonPanel.add(STATUSTEXT);

    // comments panel:
    JPanel commentsPanel = new JPanel();
    commentsPanel.setOpaque(false);
    commentsPanel.setLayout(new BoxLayout(commentsPanel,BoxLayout.PAGE_AXIS));
    commentsPanel.setBorder(BorderFactory.createTitledBorder(lbd,"Comments"));
    commentsPanel.add(jsp);

    // screenshot panel:
    JPanel screenshotPanel = new JPanel();
    screenshotPanel.setOpaque(false);
    screenshotPanel.setLayout(new BoxLayout(screenshotPanel,BoxLayout.PAGE_AXIS));
    //screenshotPanel.setBorder(BorderFactory.createTitledBorder(lbd,"Screenshot"));
    screenshotPanel.add(IMPANEL);

    // title panel:
    JPanel titlePanel = new JPanel();
    titlePanel.setOpaque(false);
    titlePanel.setBorder(BorderFactory.createTitledBorder(lbd,"Title"));
    titlePanel.setLayout(new BoxLayout(titlePanel,BoxLayout.LINE_AXIS));
    titlePanel.setPreferredSize(new Dimension(200, 42));
    titlePanel.add(LOGTITLE);
    titlePanel.add(LOGBOOKCHOICE);

    JPanel tabPanel=null;
    if (DOTABS)
    {
      tabPanel = makeTabbedPane();
      tabPanel.add(screenshotPanel);
      tabPanel.setBorder(BorderFactory.createTitledBorder(lbd,"Screenshots"));
    }

    // main frame:
    FRAME = new JFrame("JLab Logbook Entry.");//:  "+LOGBOOKNAME);
    FRAME.getContentPane().setBackground(Color.LIGHT_GRAY);
    FRAME.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    FRAME.add(commentsPanel, BorderLayout.CENTER);
    FRAME.add(buttonPanel, "South");
    FRAME.add(titlePanel, "North");
    if (DOTABS) FRAME.add(tabPanel,"West");
    else        FRAME.add(screenshotPanel,"West");
    FRAME.pack();
//    FRAME.setResizable(false);
    FRAME.setVisible(true);
  }

  public JPanel makeImagePane()
  {
    JPanel jp=new JPanel();
    jp.setPreferredSize(new Dimension(IMGWIDTH,IMGHEIGHT));
    jp.setBorder(BorderFactory.createBevelBorder(BevelBorder.LOWERED));
    jp.setOpaque(false);
    return jp;
  }

  public JPanel makeTabbedPane()
  {
    JPanel buttonPanel = new JPanel();
		buttonPanel.setLayout(new BoxLayout(buttonPanel,BoxLayout.X_AXIS));
		JButton shotButton = new JButton("Take Screenshot");
		JButton removeButton = new JButton("-");
		buttonPanel.add(shotButton);
		buttonPanel.add(ADDTABBTN);
		buttonPanel.add(removeButton);
    IMTABS = new JTabbedPane();
    SpringLayout layout = new SpringLayout();
    JPanel tabPanel = new JPanel();
    tabPanel.setLayout(layout);
    tabPanel.add(IMTABS);
    tabPanel.add(buttonPanel);
    IMTABS.setBackground(Color.LIGHT_GRAY);
		layout.putConstraint(SpringLayout.EAST, buttonPanel, 0, SpringLayout.EAST, tabPanel);
		layout.putConstraint(SpringLayout.WEST, buttonPanel, 0, SpringLayout.WEST, tabPanel);
		layout.putConstraint(SpringLayout.SOUTH, buttonPanel, 0, SpringLayout.SOUTH, tabPanel);
		layout.putConstraint(SpringLayout.EAST, IMTABS, 0, SpringLayout.EAST, tabPanel);
		layout.putConstraint(SpringLayout.WEST, IMTABS, 0, SpringLayout.WEST, tabPanel);
		layout.putConstraint(SpringLayout.NORTH, IMTABS, 0, SpringLayout.NORTH, tabPanel);
		layout.putConstraint(SpringLayout.SOUTH, IMTABS, 0, SpringLayout.NORTH, buttonPanel);
		
    ADDTABBTN.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
        int ii=IMTABS.getTabCount();
        JPanel ip=makeImagePane();
        IMPANELS.add(ip);
        IMPATHS.add("");
				IMTABS.addTab("#" + (ii + 1),ip);
				IMTABS.setSelectedIndex(IMTABS.getTabCount() - 1);
        if (DEBUG) System.out.println("Adding TabIndex "+ii);
			}
		});
    ADDTABBTN.doClick();

		removeButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
        int ii=IMTABS.getSelectedIndex();
				if (ii != -1) {
          if (DEBUG) System.out.println("Removing Tab Index "+ii);
					IMTABS.remove(ii);
          IMPANELS.get(ii).removeAll();
          IMPANELS.remove(ii);
          IMPATHS.remove(ii);
					for(int tabIndex = 0; tabIndex < IMTABS.getTabCount(); tabIndex++) {
            if (DEBUG) System.out.println("Setting TabIndex "+tabIndex+" Title ");
						IMTABS.setTitleAt(tabIndex, "#" + (tabIndex + 1));
					}
				}
			}
		});
    shotButton.addActionListener(new screenshotAction());
    buttonPanel.setOpaque(false);
    tabPanel.setOpaque(false);
    IMTABS.setOpaque(false);
    buttonPanel.setBackground(Color.LIGHT_GRAY);
    tabPanel.setPreferredSize(new Dimension(IMGWIDTH,IMGHEIGHT));
    return tabPanel;
  }

  public void forceUpdateStatusPane()
  {
    // at least one of these is important:
    STATUSTEXT.update(STATUSTEXT.getGraphics());
    STATUSTEXT.updateUI();
    STATUSTEXT.repaint();
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
    if (LOGTITLE.getText().equals(stockTitle) ||
        LOGTITLE.getText().equals(""))
    {
      updateStatusPane("ERROR:  Update Log Title Before Submitting.",Color.RED);
      return;
    }
    //LogEntry entry = new LogEntry("", LOGBOOKNAME);
    LogEntry entry = new LogEntry("", (String)LOGBOOKCHOICE.getSelectedObjects()[0]);
    //entry.setEmailNotify("rafopar@jlab.org");
    try {
      if (DOTABS)
      {
        for (int jj=0; jj<IMPATHS.size(); jj++) {
          if (IMPATHS.get(jj).equals("")) continue;
          if (DEBUG) System.out.println("Logging Image #"+jj+": "+IMPATHS.get(jj));
          entry.addAttachment(IMPATHS.get(jj),IMPATHS.get(jj));
        }
      }
      else if (!IMGPATH.equals("")) entry.addAttachment(IMGPATH,"Snapshot of "+IMGPATH);
      entry.setTitle(LOGTITLE.getText());
      entry.setBody(LOGTEXT.getText().replaceFirst("Enter Comments Here",""));
      final long logNumber = entry.submitNow();
      //entry.submit();
      //System.out.println(entry.getXML());
      if (DEBUG) System.out.println("Log #" + logNumber+" Submitted.");
      updateStatusPane("Log #"+logNumber+" Submitted.",Color.RED);
    }
    catch (Exception e) { 
      System.err.println("\nError Submitting To Logbook:\n"+e.getMessage());
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
      updateStatusPane("Last Screenshot: "+imgpath,Color.BLACK,11);
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
  class clearAction implements ActionListener
  {
    public void actionPerformed (ActionEvent e) {
      while (IMTABS.getTabCount()>1) IMTABS.remove(IMTABS.getTabCount()-1);
      IMTABS.removeAll();
      IMPATHS.clear();
      IMPANELS.clear();
      ADDTABBTN.doClick(); 
      IMTABS.updateUI();
      showScreenshot(null);
      updateStatusPane("",Color.BLACK);
      initLogTitle();
      initLogComments();
      IMGPATH=null;
    }
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
