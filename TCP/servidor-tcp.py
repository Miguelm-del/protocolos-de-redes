import socket

porta = 9060
host = 'localhost'


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((host, porta))

servidor.listen()
print("Aguardando conexão do Cliente")


conexao, endereco = servidor.accept()

print("Conectado no endereco", endereco)


while True:
    data = conexao.recv(1024)
    if not data:
        print("Conexão encerrada")
        conexao.close()  
        break
    conexao.sendall(data)
