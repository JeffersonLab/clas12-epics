<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<databrowser>
    <title></title>
    <save_changes>true</save_changes>
    <show_legend>false</show_legend>
    <show_toolbar>true</show_toolbar>
    <grid>false</grid>
    <scroll>true</scroll>
    <update_period>3.0</update_period>
    <scroll_step>5</scroll_step>
    <start>-3.00 h</start>
    <end>now</end>
    <archive_rescale>STAGGER</archive_rescale>
    <background>
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
    </background>
    <title_font>Sans|15|1</title_font>
    <label_font>Sans|10|1</label_font>
    <scale_font>Sans|9|0</scale_font>
    <legend_font>Sans|9|0</legend_font>
    <axes>
        <axis>
            <visible>true</visible>
            <name>Value 1</name>
            <use_axis_name>false</use_axis_name>
            <use_trace_names>true</use_trace_names>
            <right>false</right>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <label_font>|10|0</label_font>
            <scale_font>|10|0</scale_font>
            <min>-1.86</min>
            <max>0.54</max>
            <grid>false</grid>
            <autoscale>false</autoscale>
            <log_scale>false</log_scale>
        </axis>
        <axis>
            <visible>true</visible>
            <name>Value 2</name>
            <use_axis_name>false</use_axis_name>
            <use_trace_names>true</use_trace_names>
            <right>false</right>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <label_font>|10|0</label_font>
            <scale_font>|10|0</scale_font>
            <min>-1.6</min>
            <max>1.02</max>
            <grid>false</grid>
            <autoscale>false</autoscale>
            <log_scale>false</log_scale>
        </axis>
        <axis>
            <visible>true</visible>
            <name>Value 3</name>
            <use_axis_name>false</use_axis_name>
            <use_trace_names>true</use_trace_names>
            <right>false</right>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <label_font>|10|0</label_font>
            <scale_font>|10|0</scale_font>
            <min>-0.68</min>
            <max>0.85</max>
            <grid>false</grid>
            <autoscale>false</autoscale>
            <log_scale>false</log_scale>
        </axis>
        <axis>
            <visible>true</visible>
            <name>Value 4</name>
            <use_axis_name>false</use_axis_name>
            <use_trace_names>true</use_trace_names>
            <right>false</right>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <label_font>|10|0</label_font>
            <scale_font>|10|0</scale_font>
            <min>-0.42</min>
            <max>1.07</max>
            <grid>false</grid>
            <autoscale>false</autoscale>
            <log_scale>false</log_scale>
        </axis>
        <axis>
            <visible>true</visible>
            <name>Value 5</name>
            <use_axis_name>false</use_axis_name>
            <use_trace_names>true</use_trace_names>
            <right>false</right>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <label_font>|10|0</label_font>
            <scale_font>|10|0</scale_font>
            <min>-0.25</min>
            <max>1.93</max>
            <grid>false</grid>
            <autoscale>false</autoscale>
            <log_scale>false</log_scale>
        </axis>
        <axis>
            <visible>true</visible>
            <name>Value 6</name>
            <use_axis_name>false</use_axis_name>
            <use_trace_names>true</use_trace_names>
            <right>false</right>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <label_font>|10|0</label_font>
            <scale_font>|10|0</scale_font>
            <min>0.06</min>
            <max>1.16</max>
            <grid>false</grid>
            <autoscale>false</autoscale>
            <log_scale>false</log_scale>
        </axis>
    </axes>
    <annotations>
    </annotations>
    <pvlist>
        <pv>
            <display_name>B_SVT_HV_R1T:outputMeasCurrent:avg</display_name>
            <visible>true</visible>
            <name>B_SVT_HV_R1T:outputMeasCurrent:avg</name>
            <axis>0</axis>
            <color>
                <red>255</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsappa.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsappb.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=prod_controls)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>B_SVT_HV_R1B:outputMeasCurrent:avg</display_name>
            <visible>true</visible>
            <name>B_SVT_HV_R1B:outputMeasCurrent:avg</name>
            <axis>1</axis>
            <color>
                <red>245</red>
                <green>0</green>
                <blue>255</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsappa.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsappb.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=prod_controls)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>B_SVT_HV_R2T:outputMeasCurrent:avg</display_name>
            <visible>true</visible>
            <name>B_SVT_HV_R2T:outputMeasCurrent:avg</name>
            <axis>2</axis>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>255</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsappa.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsappb.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=prod_controls)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>B_SVT_HV_R2B:outputMeasCurrent:avg</display_name>
            <visible>true</visible>
            <name>B_SVT_HV_R2B:outputMeasCurrent:avg</name>
            <axis>3</axis>
            <color>
                <red>0</red>
                <green>124</green>
                <blue>255</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsappa.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsappb.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=prod_controls)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>B_SVT_HV_R3T:outputMeasCurrent:avg</display_name>
            <visible>true</visible>
            <name>B_SVT_HV_R3T:outputMeasCurrent:avg</name>
            <axis>4</axis>
            <color>
                <red>0</red>
                <green>128</green>
                <blue>0</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsappa.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsappb.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=prod_controls)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <display_name>B_SVT_HV_R3B:outputMeasCurrent:avg</display_name>
            <visible>true</visible>
            <name>B_SVT_HV_R3B:outputMeasCurrent:avg</name>
            <axis>5</axis>
            <color>
                <red>68</red>
                <green>210</green>
                <blue>80</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsappa.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsappb.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=prod_controls)))</url>
                <key>1</key>
            </archive>
        </pv>
    </pvlist>
</databrowser>