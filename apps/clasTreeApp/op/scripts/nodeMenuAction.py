from org.csstudio.opibuilder.scriptUtil import PVUtil,WidgetUtil,ConsoleUtil




#This one of a pair of partner scripts nodeMenuAction.py and nodeMenuUpdate.py
#Together they are used to choose a NODE in the epics tree.
#There is a node selection menu for each level in the hierarchy 
#Each time the NODE is modified, all menus call nodeMenuUpdate.py.
#Each menu then sets its state and list of choices according to the loaded dictionary of nodes.

#They would be run inside allNodeMenuContainer.opi, which needs to be called wth a macro specifying
#the initial node, and the maximum depth. Eg. defaults P="B", NTOT=6.

#When a choice is made in one of the menus,
#loc://$(LCID)_MOUT  (pv[1]) is changed, tiggering nodeMenuAction.py for ChoiceButton_N, which makes
#loc://$(LCID)_NODE  (pv[0]) change, triggering nodeMenuUpdate.py for all buttons.
#Warning - some danger of infinite recursion here. Careful"

#The $(LCID) macro is used to make local PVs per instance. So several instances could be run from the same CSS
#without interfering.


#For example loc://$(LCID)_NODE pv is like this:         B_SYS_HV_ECAL_SEC1_.....
#split into list with elements                           0 1   2  3    4    5
#eg - with N for the menu N = 3                                   *
#
# 3 clicked to set DC changes loc://$(LCID)_NODE pv to   B_SYS_HV_DC


n = int(widget.getMacroValue("N"))               #Get N,TOP and NODE and MOUT_$(N)
topnode=widget.getMacroValue("TOP")
node = PVUtil.getString(pvArray[0])
sel = PVUtil.getString(pvArray[1])

nlist=node.split("_")                           #make a list of the parts of node   nlist = (B,SYS,HV,ECAL,SEC1,....)

#ConsoleUtil.writeInfo("Action:"+str(n)+",  mode= "+node+",  sel= "+sel)
if not sel == 'select..':
        if n>=len(nlist) or ((n<len(nlist)) and (not sel==nlist[n])):
        
                newnode=topnode
                if n>=1:
                        for e in range(1,n):
                                newnode+="_"+nlist[e]
                newnode+="_"+sel
                pvArray[0].setValue(newnode)       

