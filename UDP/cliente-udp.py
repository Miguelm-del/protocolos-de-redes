import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

porta = 15000
host = 'localhost'

while True:
    mensagem_enviar = input("Impute a mensagem: ")

    cliente.sendto(mensagem_enviar.encode(), (host, porta))

    print("Mensagem do servidor: ")
    mensagem_bytes, endereco_servidor = cliente.recvfrom(2048)

    print(mensagem_bytes.decode())
