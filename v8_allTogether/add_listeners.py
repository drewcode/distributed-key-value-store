from kazoo.client import KazooClient
from kazoo.client import KazooState
import socket
import sys



#Kazoo-states listener function
def my_listener2(state): 
	if state==KazooState.LOST :
		pass
		#print("2lost") 
	elif state==KazooState.CONNECTED :
		pass
		#3print("2Connected") 
	else :
		zk = KazooClient(hosts='127.0.01:2181')
		zk.start()
		if zk.exists("/testing/downnode") == None :
			zk.ensure_path("/testing/downnode")			
			zk.create("/testing/downnode", 1)
		print(state)

def my_listener3(state): 
	if state==KazooState.LOST :
		pass
		#print("3lost") 
	elif state==KazooState.CONNECTED :
		pass
		#print("3Connected") 
	else :
		zk = KazooClient(hosts='127.0.01:2181')
		zk.start()
		if zk.exists("/testing/downnode") == None :
			zk.ensure_path("/testing/downnode")			
			zk.create("/testing/downnode", 2)
		print(state)

data = sys.argv[1].split()
#data = count+" "+master+" "+node1+" "+node2+" "+node3

zk2 = KazooClient(hosts=data[3])
zk2.add_listener(my_listener2)
zk3 = KazooClient(hosts=data[4])
zk3.add_listener(my_listener3)
