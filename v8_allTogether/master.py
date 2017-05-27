from kazoo.client import KazooClient
import socket
import sys

host = '127.0.0.1'
port = 6066

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

dic = {}
flag = -1

# Accept the connection 
(conn, addr) = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

#recieve meta data about cluster
giff = conn.recv(1024)
if giff == "GIFF":
	conn.send(sys.argv[1])

while True:

	if zk.exists("/testing/downnode1") != None :
		flag = 1
	if zk.exists("/testing/downnode2") != None :
		flag = 2	

	ack_data = conn.recv(1024)
	if ack_data == 'OK?' :	
		if flag >= 0:
			conn.send(flag)
		else:
			conn.send('OK')

	data = conn.recv(1024)
	if data == 'ignore':
		continue

	tokens = data.split()  
	command = tokens[0]                   

	# -- key = tokens[1]
	# -- val = tokens[2]

	if command == 'get':                    
		if dic.has_key(tokens[1]) :
			conn.send(dic[tokens[1]])
		else:
			conn.send('record not found')

	elif command == 'put':                
		dic[tokens[1]] = tokens[2]           
		conn.send('inserted')
		print "inserted here"                      

	elif command == 'quit':                 
		conn.send('quit')                 
		break                             

	else:
		break
		
zk.stop()		
conn.close() 