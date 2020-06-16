import socket

server_soc = socket.socket()

#where to listne???
#server_soc.bind(('127.0.0.1',5000)) # this is the local host (loopac)
#server_soc.bind(('0.0.0.0',5000)) # this means packet socket will get the current ip of the kernel
server_soc.bind(('192.168.1.17',5000)) # connect from my ipv4

#backlog - how many can wait while the server is bussy (max buffer size - queue)
server_soc.listen(1)

# loop on spesific client in queue
while True:
    print('Server is Listening....')
    (client_soc, client_address) = server_soc.accept() # starts listening and returns tuple when recieves
    print('starting connection with client: ' + str(client_address))

    #loop until exis msg
    while True:
        name = client_soc.recv(1024) #size of buffer int bytes to listen to...
        if name.decode('utf-8') == 'exit':
            break
        # 'Hello ' + name.decode('utf-8') is string
        # then we will encode the string back to bytes!
        client_soc.send(('Hello ' + name.decode('utf-8')).encode('utf-8')) 

    client_soc.close()
    print('Closing connection...')

server_soc.close()
print('Closing listener...')