import socket


#get ips - dynamically - from ensemble  

#assign shit
MASTER = 0
NUM = 3			#dynamic all 3

flag = -1

server = ['127.0.0.1', '127.0.0.1', '127.0.0.1']			 
port = [6066, 6067, 6068]  									

s = []
for sv_no in range(0,NUM) :
	s.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
	s[sv_no].connect((server[sv_no],port[sv_no]))

while True:

	s[MASTER].send("OK?")
	ack = s[MASTER].recv(1024)
	if(ack != 'OK'):
		flag = ack

	command = raw_input('Enter your command: ')
	if(command == ''):
		print "Enter Something !"
		continue

	tokens = command.split()
	if(tokens[0] != 'get' and tokens[0] != 'put' and tokens[0] != 'quit') :
		print "Erroneous command, type the right command please !"
		continue

	if(tokens[0] == "quit") :
		for sv_no in range(0, NUM) :
			if(sv_no != flag) :
				s[sv_no].send(command)
		print 'Exiting...'
		break

	elif(tokens[0] == "get") :
		alphabet_position = ord((tokens[1][0]).lower()) - 97
		region = alphabet_position / (26 / NUM)
		
		if region >= NUM :
			region = NUM - 1
		if region == flag:
			region = (region+1) % NUM
		if region == 1 or region == 2:
			s[MASTER].send("ignore")

		sv = s[region]
		sv.send(command)
		reply = sv.recv(1024)
		print reply

	else :
		alphabet_position = ord((tokens[1][0]).lower()) - 97
		region = alphabet_position / (26 / NUM)
		if region >= NUM :
			region = NUM - 1

		if region == 1:
			s[MASTER].send("ignore")

		if region != flag:
			sv = s[region]
			sv.send(command)
			reply = sv.recv(1024)
			#print reply

		if (region+1)%NUM != flag:
			sv = s[(region+1)%NUM]		
			sv.send(command)
			reply = sv.recv(1024)
			print reply