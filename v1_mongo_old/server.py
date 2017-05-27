import socket
from pymongo import MongoClient

client = MongoClient()
db = client.test

host = '127.0.0.1'
port = 6066

s = socket.socket()
s.bind((host,port))
s.listen(1)

# Accept the connection 
(conn, addr) = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])
while True:
	data = conn.recv(1024)

	tokens = data.split()  
	command = tokens[0]                   

	if command == 'get':                    
		cursor = db.randomcoll.find({'key' : tokens[1]})
		results = ''
		if cursor.count():
			for record in cursor:
				results += record['val'] + ' '	
			conn.send(results)
		else:
			conn.send('record not found')

	elif command == 'put':                
		db.randomcoll.insert({'val' : tokens[2], 'key' : tokens[1]})           
		conn.send('inserted')                      

	elif command == 'quit':                 
		conn.send('quit')                 
		break                             

conn.close() 