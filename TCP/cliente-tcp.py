import socket


porta = 9060
host = 'localhost'

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


cliente.connect((host,porta))



cliente.sendall(str.encode("Hello World")) 


data = cliente.recv(1024) 

print("Mensagem ecoada:", data.decode())



