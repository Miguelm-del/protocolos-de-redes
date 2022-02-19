import socket #Importação da biblioteca socket para utilizar seus metodos/funções

#Socket é a biblioteca que utilizamos para conectar dois hosts pela rede, utilizando a camada de aplicação que passa pela camada de transporte, a unica interação que fazemos com a camada de transporte é falar qual o tipo é o protocolo

#Precisamos ter um socket da mesma forma que foi feito o nosso servidor, ambos tem que ser do mesmo socket para sua copatibilidade

#Criação do socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#AF_INET - Tipo ipv4
#SOCK_DGRAM - Utilizar o protocolo tipo UDP

#Não é preciso se aprensentar (HandShake - aperto de mão)

# Precisamos ter a mesma porta do servidor e mesmo endereço

porta = 15000
host = 'localhost' #Localhost 






#Vamos fazer um loop infinito para enviar os dados

while True:
    mensagem_enviar = input("Digite a mensagem: ") #Mensagem que séra enviada para o servidor
    
    #vamos da um sendto para enviar para o servidor, utilizando a mensagem e o endereço do servidor e a porta
    
    cliente.sendto(mensagem_enviar.encode(),(host,porta))
    
    
    #Receber do servidor
    
    print("Mensagem Recebida do Servidor: ")
    mensagem_bytes, endereco_servidor = cliente.recvfrom(2048)
    
    print(mensagem_bytes.decode())