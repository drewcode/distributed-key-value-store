
cd zookeeper-3.5.2-alpha/bin 	#go to your zookeeper bin directory
#cmd1="./zkServer.sh stop" 
#$cmd1 
cmd="./zkServer.sh start" 
$cmd 
echo "Working..."
sleep 5
cd ../.. 						#go to the directory which has the python code

python ensemble_znodes_creation.py
echo "Working..."
sleep 15 


python get_ips.py > all_vals
python add_listeners.py $all_vals
python master.py $all_vals
