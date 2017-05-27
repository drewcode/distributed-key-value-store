import socket


#get ips - dynamically - from ensemble  

#assign ranges
server = ['127.0.0.1', '127.0.0.1', '127.0.0.1']			 
port = [6066, 6067, 6068]  									

s = ["" , "", ""]
for i in range(0,3) :
	s[i] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s[i].connect((server[i],port[i]))



while True:

	command = raw_input('Enter your command: ')
	if(command == ''):
		print "Enter Something !"
		continue

	tokens = command.split()
	if(tokens[0] != 'get' and tokens[0] != 'put' and tokens[0] != 'quit') :
		print "Erroneous command, type the right command please !"
		continue

	if(tokens[0] == "quit") :
		s[0].send(command)
		s[1].send(command)
		s[2].send(command)
		print 'Exiting...'
		break

	else :
		key_letter = ord((tokens[1][0]).lower())
		if(key_letter < 105) :
			sv = s[0]
		elif(key_letter < 114) :
			sv = s[1]
		else :
			sv = s[2]

		sv.send(command)

		reply = sv.recv(1024)
		print reply
