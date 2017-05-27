import socket

SERVER = '127.0.0.1'  
PORT = 6066  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER,PORT))

while True:
	command = raw_input('Enter your command: ')
	s.send(command)

	reply = s.recv(1024)

	if reply == 'quit':
		break
		print 'Exiting...'

	print reply
