from kazoo.client import KazooClient
from kazoo.client import KazooState
import time
import socket

#retrieving ip address
s= socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
myip = s.getsockname()[0] 

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

#check if path exists, if not, this is the first node that's coming up
if zk.exists("/testing") == None :
	zk.ensure_path("/testing")			
	zk.create("/testing/master", myip)
	zk.create("/testing/node1",myip)
	zk.create("/testing/count","1")

#for all other nodes that come up
else :
	data, stat = zk.get("/testing/count")	#gets each node
	data1 = int(data)+1 					#gets data from count , increments it
	zk.set("/testing/count",str(data1)) 	#puts it back
	name = "node"+str(data1) 				#node name created using count (node2,node3)
	zk.create("/testing/node"+str(data1),myip)

time.sleep(10)	
	