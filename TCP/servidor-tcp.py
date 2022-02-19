from ast import While
import socket #Importação da biblioteca/modulo socket para utilizar seus metodos/funções , IP e Numero de porta


#Criando Sockets, utilizando classe socket da biblioteca socket
porta = 9060
host = 'localhost'


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#(family-familia e type-tipo)

# AF_INET Familia IPv4  / SOCK_STREAM tipo TCP

#Servidor TCP vai ficar escutando e aceitando conexões

#Agora vamos usar a função bind , que reque da porta e o host

#O parenteses duplo é que o metodo bind recebe só um parametro, mas esse parametro é divido em duas partes, por isso colocamos os dois parametros dentro de um parenteses ficando só um parametro para o metodo

servidor.bind((host,porta)) #Vinculamos agora o nosso servidor com o nosso host e nossa porta

#Agora vamos colocar para escutar
servidor.listen()
print("Aguardando conexão do Cliente") 


#Agora nosso servidor precisa aceitar a conexão

conexao, endereco  = servidor.accept() #accept meto de aceitar
   
print("Conectado no endereco", endereco)


#Agora trocar mensagem

#Fazer um loop infinito
while True: 
    data = conexao.recv(1024) #Tamanho maximo bytes que serão recebidos e guardados em data
    if not data:
        print("Fechando a conexão")
        conexao.close() #Encerrar conexao
        break
    conexao.sendall(data)