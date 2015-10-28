#!/bin/sh

#############################################################################################
#this is the main function which gets called recursively to go through the detector hierarchy
#############################################################################################
get_node_info(){
    
    #args: node, depth which must be local variables 
    
    local node=$1;
    local depth=$2;
    local d=`expr $depth + 1` 
    ElementNames=""; #default to 0 elements and subnodes
    SubNodeNames="";

    if [ $mode = "fs" ]; then  #get the info from the nodeInfo.txt files in the filesystem
	nodeInfo="${node}/nodeInfo.txt";        
	NodeName=`grep NodeName: $nodeInfo | awk '{print $2}'`
	SubNodeCount=`grep SubNodeCount: $nodeInfo | awk '{print $2}'`
	if [ $SubNodeCount != "0" ]; then
	    SubNodeNames=`grep SubNodeNames: $nodeInfo | awk '{gsub("SubNodeNames:","");print $0}'`
	fi
	ElementCount=`grep ElementCount: $nodeInfo | awk '{print $2}'`
        if [ $ElementCount != "0" ]; then
	    ElementNames=`grep ElementNames: $nodeInfo | awk '{gsub("ElementNames:","");print $0}'`
	fi
	
    else # Get the  information from EPICSBSIM_HV_PCAL_SEC6_V_E28:pwonoff
	NodeName=${node}
	SubNodeCount=`caget -t ${NodeName}:SubNodeCount`
	if [ $SubNodeCount != "0" ]; then
	    SubNodeNames=`caget -t -S ${NodeName}:SubNodeNames`
	fi
	ElementCount=`caget -t ${NodeName}:ElementCount`
        if [ $ElementCount != "0" ]; then
	    ElementNames=`caget -t -S ${NodeName}:ElementNames`
	fi
    fi
    
     echo "${indent[d]}${NodeName} ... Doing $SubNodeCount subnodes: $SubNodeNames";
    echo
    
    #loop over all subnodes calling this function for each one
    #oh lovely recursion.

    
    for subnode in $SubNodeNames;
    do
	#echo "${indent[d]}$subnode";
	fullsub="${node}${delim}${subnode}";
	get_node_info $fullsub $d;
	echo
    done

    echo "${indent[d]}${NodeName} ... Doing $ElementCount elements: $ElementNames";
    echo
    for element in $ElementNames;                                #for each element
    do
	if [ "$command" = "#" ]; then
	    echo "${indent[d]}${NodeName}_$element:${pv} ";
	else
	    echo -n "${indent[d]}${NodeName}_$element:${pv} ";
	    echo -n "Command = \"$command  ${NodeName}_$element:${pv} $user_args\""
	    res=`eval $command ${NodeName}_$element:${pv} $user_args`;     #run command element user_args ans save result
	    echo "      Result = \"$res\"";
	    elresult="$elresult $res";                               #add result to all
	fi
    done
    
    echo -n "${indent[d]}${NodeName} Done";
    if [ $nodecom = "y" ]; then                                  #if we run the command on subnodes as well as elements
	#call the command with the subnode name, user arge and the total result of running the command on all the elements
	res=`eval $command $user_args${NodeName} $elrusult`;     #run command element user_args ans save result
	echo "Result = \"$res\"";
    else
	echo "";
    fi
    echo;
}
####################################################################################################


##########################################################################
usage(){
    echo "Usage: $progname [-m mode] [-p pvname] <topnode> [<command> <args....>]"
    exit 0
}
##########################################################################


###################################################################################################
#
#This is the start of the script, which sets up how to call the recursive get_node_info() function.
#
###################################################################################################

# -----some initial values, which may be overridden by args----------------------------------------
#make an array of strings for efficient indentation

istring="";
for n in 0 1 2 3 4 5 6 7 8 9;
do
    indent[n]=$istring;
    istring="$istring  "; #add 2 spaces foe each depth
done

command="#";              #default command called for every node and element is just a comment
nodecom="n";              #don't run command for nodes, only elements
depth=0;                  #starting depth in the hierarchy
mode="epics";             #mode for getting node into (= epics or fs)
delim="_";                #delimiter for nodes
pv="";                    #default to empty pv name

# -------------------------------------------------------------------------------------------------




###################################################################################################
# Process the arguments to the programm and call the recursive function
###################################################################################################

progname=$0               #get prog name from arg         

if [ $# -lt "1" ]; then   #if no args or opts, usage
    usage;
fi

while getopts ":m:p:hs" opt; do #check for options
    case $opt in
	m )  mode=$OPTARG ;;
	p )  pv=$OPTARG ;;
	s )  nodecom="y" ;;
	h )  usage ;;
	\?)  usage ;;
    esac
done
shift $((OPTIND - 1));

topnode=$1;                 #get top node
if [ $# -gt "1" ]; then     #if no args or opts, usage
    command=$2;             #get user command
    nuarg=`echo "$command"| awk '{print 2+NF}'` #If command in quotes, make user args start after quotes
fi

if [ $mode = "fs" ]; then
   delim="/";
fi
   
user_args=`echo $@ | awk -v nuarg=$nuarg '{for(n=nuarg;n<=NF;n++)printf"%s ",$n}'`
eptopnode=`echo $topnode | awk '{gsub("/","_");print $0}'` # replace and \'s with _ (if coming from fs, not epics)

#echo "Command = $command";
#echo "args = \"$user_args\"";
#exit;
#echo $topnode;
#start to plough through the hierarchy from the top node. 
get_node_info $topnode $depth;
exit;
#####################################################################################################
