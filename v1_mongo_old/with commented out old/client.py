import socket

HOST = '127.0.0.1'  
PORT = 6066  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
	command = raw_input('Enter your command: ')
		#print command
	    #if command.split(' ',1)[0]=='put' || command.split(' ',1)[0]=='get':
	    # while True:    
	    #     while True:
	    #         text = raw_input()
	    #         print text
	    #         command = command+'\n'+text
	    #         if text == '.':
	    #             break
	s.send(command)
    #else :
    #while True:
	reply = s.recv(1024)

	if reply == 'quit':
		break
		print 'Exiting...'

	elif reply == 'inserted' or reply == 'record not found':
		print reply
	else:
		replies = reply.split()
		for r in replies:
			print r
    #if reply == 'Quit':
    #   	break

    
    