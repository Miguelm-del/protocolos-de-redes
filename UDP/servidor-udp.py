from ast import While
import socket  #Importação da biblioteca socket


#Quando se utilizar UDP não precisamos fazer um handshake, não precisa se conectar, se apresentar, estabelecer uma conexão para depois começar enviar dados.

#Simplismente abre uma porta é o cliente conectar naquela porta, é já pode enviar dados

#Criar um socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#AF_INET - Tipo ipv4
#SOCK_DGRAM - Utilizar o protocolo tipo UDP



#Agora vamos usar a função bind , que reque da porta e o host

porta = 15000
host = '' #Localhost 

servidor.bind((host,porta))
print('Escutando...')

#Agora precisamos de um loop eterno para ficar sempre escutando e lendo esse socket

while True:
    #funcao recvfrom e o tamanho de dados que vamos utilizar 2048, receber os bytes e depois o endereço, vamos receber os dados em bytes
    
    #Vamos utilizar duas variaves como foi utilizado na função bind
    
    mensagem_bytes, endereco_cliente = servidor.recvfrom(2048)
    print("Mensagem recebida cliente:")
    mensagem_resposta = mensagem_bytes.decode() #Pegar os bytes e transformar em string
    print(mensagem_resposta)
    
    
    servidor.sendto(mensagem_resposta.encode(), endereco_cliente)
    
   
    