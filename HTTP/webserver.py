# Temos um código chamado "webserver.py", que ele ira iniciar um servidor web, codigo feito em python. Em seguida, sempre que enviarmos uma solicitação para o servidor séra ecoado de volta os cabeçalhos e qualquer dado que foi enviado como parte da solicitação e vai responder esses dados como uma resposta HTTP, temos assim o nosso Servidor Ecoador Tabajara.

# Vamos utilizar o curl para testar o nosso servidor:

# Fazendo uma solicitação POST, enviando algum dado para o servidor

#curl localhost:8080 -d “Ola Mundo” 

#-------------------------------------------

PORTA = 8080 #Porta que utilizaremos
HOST = 'localhost' # Vamos utilizar "localhost" vamos então o nosso endereço local ( nossa maquina como um servidor).


from http.server import HTTPServer, BaseHTTPRequestHandler
#Importação das classes HTTPServer e BaseHTTPRequestHandler que estão disponiveis na biblioteca http.server

#A classe HTTPServer vai executar nosso servidor

#A classe BaseHTTPRequestHandler (Manipulador de requisição HTTP básico), essa classe é usada para lidar com as solicitações HTTP que chegam ao servidor. Por si só ele não pode responder a nenhuma solicitação HTTP real, por isso iremos subclassificar, para assim lidar com os seus métodos.

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler): # Agora podemos usar os métodos(funções) e suas variaveis da classe BaseHTTPRequestHandler
   
   # Ele ira ouvir solicitações GET e POST e apenas ecoa o cabeçalho e os dados do corpo que foram enviados
   
   def do_GET(self):
        
