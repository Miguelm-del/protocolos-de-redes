import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


porta = 15000
host = ''

servidor.bind((host, porta))
print('....Escutando')


while True:

    mensagem_bytes, endereco_cliente = servidor.recvfrom(2048)
    print("Mensagem recebida cliente:")
    mensagem_resposta = mensagem_bytes.decode()
    print(mensagem_resposta)

    servidor.sendto(mensagem_resposta.encode(), endereco_cliente)
