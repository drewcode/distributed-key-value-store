import socket

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
		if dic.has_key(tokens[1]) :
			conn.send(dic[tokens[1]])
		else:
			conn.send('record not found')

	elif command == 'put':                
		dic[tokens[1]] = tokens[2]           
		conn.send('inserted')                      

	elif command == 'quit':                 
		conn.send('quit')                 
		break                             

	else:
		break
		
conn.close() 