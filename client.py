import socket

SERVER_HOST = '192.168.1.17'
PORT = 5000
ADDR = (SERVER_HOST, PORT)

# socket.AF_INET - layer level 3 (Socket type)
# socket.SOCK_STREAM - layer level 4 (socket kind - tcp byte streaming wich means all the data passes and waiting in chuncks the stream in tcp order)
# socket.DGRAM - socket king not streaming, used for very short and speedy msgs....
my_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting
my_soc.connect(ADDR)

#loop msg
while True:
    outdata = input('Enter your name: ')
    my_soc.send(outdata.encode('utf-8'))
    if outdata == 'exit':
        break    
    indata = my_soc.recv(1024)
    print(indata.decode('utf-8'))
    
print("Client Exit...")
my_soc.close()