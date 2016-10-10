# EtherIP settings

### EIP_buffer_limit
Now set to 450 bytes.  Default of 500 eventually caused: 
"CIP_MultiRequest reply: invalid service 0x52"

When this happens, a series of PVs will disconnect and reconnect.  In our case 
we saw that while issuing a new setpoint and somethings continuously.  

On the Rockwell manual for the PLC labels 0x52 as "Read Tag Fragmented Service 
(Request)".  It states that the data will not fit into a single packet (approx. 
500 bytes).  This is the EIP_buffer_limit default.  Setting it larger created 
the same issue.  Lowering to 450 worked and is also used in Hall D Solenoid 
software.  The EPICS EtherIP documentation admits the details for this buffer 
size are "hairy".

