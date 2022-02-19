import socket
#Vamos importar a biblioteca socket para utilizar suas funções.etc

#Utilizar mesmo host e porta do servidor, nosso servidor esta escutando na porta 9060

porta = 9060
host = 'localhost'

#Se a porta for diferente nosso servidor irá negar nossa conexao

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#(family-familia e type-tipo)

# AF_INET Familia IPv4  / SOCK_STREAM tipo TCP

#Servidor TCP vai ficar escutando e aceitando conexões

#-Agora vamos conectar nesse socket

cliente.connect((host,porta))

#Agora vamos enviar os dados para o servidor

cliente.sendall(str.encode("Hello World")) #Enviar mensagem para o servidor


data = cliente.recv(1024) #Retornar os dado do servidor

#Exibir na tela o retorno da comunicação, mensagem ecoada
print("Mensagem que foi ecoada:", data.decode())



