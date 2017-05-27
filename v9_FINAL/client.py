import socket

ip = '192.168.43.73'		#Master's IP

#retrieve ips from master
data_source = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data_source.connect((ip,6066))
data_source.send("GIFF")
data = data_source.recv(1024)
#data = count+" "+master+" "+node1+" "+node2+" "+node3

metadata = data.split()

#assign respective fields
MASTER = 0
NUM = int(metadata[0])			
flag = -1
#the IPs of three servers retrieved
server = metadata[2:5]  									
s = [data_source]			
print "These are the IPs of the servers : ", server

#socket connections to all servers set up
for sv_no in range(1,NUM) :
	s.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
	s[sv_no].connect((server[sv_no],6066))



while True:

	#get commandcfrom user
	command = raw_input('Enter your command: ')
	if(command == ''):
		print "Enter Something !"
		s[MASTER].send("ignore")		#to reset master to start
		continue

	#To check if all nodes are still up
	s[MASTER].send("OK?")
	ack = s[MASTER].recv(1024)
	if(ack != 'OK'):
		flag = int(ack)

	#sanity check
	print "master sent", ack

	tokens = command.split()
	#validate the command
	if(tokens[0] != 'get' and tokens[0] != 'put' and tokens[0] != 'quit') :
		print "Erroneous command, type the right command please !"
		continue

	#close and exit
	if(tokens[0] == "quit") :
		for sv_no in range(0, NUM) :
			if(sv_no != flag) :
				s[sv_no].send('quit')
		print 'Exiting...'
		break

	elif(tokens[0] == "get") :
		#assign region : which server
		alphabet_position = ord((tokens[1][0]).lower()) - 97
		region = alphabet_position / (26 / NUM)
		
		#making slight change, coz region sizes as 8,8,10
		if region >= NUM :
			region = NUM - 1
		#check if that region server is down
		if region == flag:
			region = (region+1) % NUM
		#to reset master since master isnt used this time
		if region == 1 or region == 2:
			s[MASTER].send("ignore")

		#get the value
		sv = s[region]
		sv.send(command)
		reply = sv.recv(1024)
		print reply

	else :			#if its a put
		#same logic as above
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
			
		if (region+1)%NUM != flag:
			sv = s[(region+1)%NUM]		
			sv.send(command)
			reply = sv.recv(1024)
			
		print reply
