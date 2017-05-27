import socket
#from pymongo import MongoClient

#client = MongoClient()
#db = client.test

host = '127.0.0.1'
port = 6066

s = socket.socket()
s.bind((host,port))
s.listen(1)

dic = {}

# Accept the connection 
(conn, addr) = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])
while True:
	data = conn.recv(1024)

	tokens = data.split()  
	command = tokens[0]                   

	# -- key = tokens[1]
	# -- val = tokens[2]

	if command == 'get':                    
		#cursor = db.randomcoll.find({'key' : tokens[1]})
		#results = ''
		#if cursor.count():
		#	for record in cursor:
		#		results += record['val'] + ' '	
		#	conn.send(results)
		if dic.has_key(tokens[1]) :
			conn.send(dic[tokens[1]])
		else:
			conn.send('record not found')

	elif command == 'put':                
		#db.randomcoll.insert({'val' : tokens[2], 'key' : tokens[1]})
		dic[tokens[1]] = tokens[2]           
		conn.send('inserted')                      

#	OVERWRITE CHOICE
#		if dic.has_key(tokens[1]) :
#			ch = raw_input("Do u wish to overwrite(y/n)")
#			dic[tokens[1]] = tokens[2] if ch == 'y' else conn.send('retained old value')
#		else:
#			dic[tokens[1]] = tokens[2]


	elif command == 'quit':                 
		conn.send('quit')                 
		break                             

conn.close() 