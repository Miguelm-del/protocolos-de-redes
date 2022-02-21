# Temos um código chamado "webserver.py", que ele ira iniciar um servidor web, codigo feito em python. Em seguida, sempre que enviarmos uma solicitação para o servidor séra ecoado de volta os cabeçalhos e qualquer dado que foi enviado como parte da solicitação e vai responder esses dados como uma resposta HTTP, temos assim o nosso Servidor Ecoador Tabajara.

# Vamos utilizar o curl (o cURL é uma abreviação para "URL do cliente") para testar o nosso servidor:

# Fazendo uma solicitação POST, enviando algum dado para o servidor

#curl localhost:8080 -d “Ola Mundo” 

#-------------------------------------------

PORTA = 8080 #Porta que utilizaremos
HOST = 'localhost' # Vamos utilizar "localhost", logo o nosso endereço local ( nossa maquina como um servidor).


from http.server import HTTPServer, BaseHTTPRequestHandler
#Importação das classes HTTPServer e BaseHTTPRequestHandler que estão disponiveis na biblioteca http.server

#A classe HTTPServer vai executar nosso servidor

#A classe BaseHTTPRequestHandler (Manipulador de requisição HTTP básico), essa classe é usada para lidar com as solicitações HTTP que chegam ao servidor. Por si só ele não pode responder a nenhuma solicitação HTTP real, por isso iremos subclassificar, para assim lidar com os seus métodos.

class cabecalho(BaseHTTPRequestHandler):
   # A classe cabecalho irá estender( No caso herdar/pegar suas varias e funções) de BaseHTTPRequestHandler, e Agora podemos usar as funções e suas variaveis da classe BaseHTTPRequestHandler

   
   #ira ouvir solicitações GET e POST e apenas ecoa o cabeçalho e os dados do corpo que foram enviados
   
   #  Usando a palavra-chave “self” podemos acessar os atributos e métodos da classe. Ele liga os atributos com os argumentos fornecidos.
  
   def do_GET(self): # Caso o cliente fazer uma requisição GET
       self.escrever_resposta(b"Hello World")
     

   def do_POST(self): #Quando o cliente fazer uma requisição( acessar o corpo do POST no método do_POST)
       #Extrair o corpo da mensagem HTTP
        tamanho_dado = int(self.headers.get('content-length', 0)) # tamanho do conteudo, e valor padrao = 0, porque se não estiver definido daria typeerror
        corpo = self.rfile.read(tamanho_dado) # para ler os dados   
       
        self.escrever_resposta(corpo) # E agora vamos exibi-lo

   def escrever_resposta(self, dados): #Função
        self.send_response(200) #Codigo de cabeçalho para dizer que esta ok
        self.end_headers() #Fechar cabeçalho
        self.wfile.write(dados) #para escrever

        print(self.headers) #Exibir o cabeçalho http
        print("Retorno: ",dados.decode('utf-8')) # Transformando a mensagem em string, com o padrao UTF-8 e dando um print para exibi-la já formatada
  
  
      
print(f"Escutando no endereço: http://{HOST}:{PORTA}\n")

#Agora nosso Servidor

servidor = HTTPServer((HOST,PORTA),cabecalho)  # onde ele pega o host e a porta, é como segundo parametro temos a classe que ele vai rodar, que foi o que foi mostrado a cima
servidor.serve_forever() # Lidar com solicitação até o desligamento
 





   # def do_GET(self): #Função GET da classe BaseHTTPRequestHandler
   #    self.send_response(200) #Codigo para sucesso ou ok para o cabeçalho 
   #    self.end_headers()#Finalizar o cabeçalho
   #    self.wfile.write(dado)
   #    print(self.headers) #Printar os cabeçalhos
   #    print(dado.decode('utf-8')) #Pegando a mensagem em bytes e transformar em texto, com o padrao utf-8
   #    dado = self.wfile.write(b'') # recebendo o dado
      
        
   # def do_POST(self):
   #    dado_tamanho = int(self.headers.get('dado_tamanho',0))
   #    corpo = self.rfile.read(dado_tamanho)
      
   #    self.send_response(200)
   #    self.end_headers()
   #    self.wfile.write(corpo)
   #    print(corpo)
   #    print(self.headers)
   #    print(corpo.decode('utf-8'))
   
   
      # def do_GET(self):
      #  # self.escrever_resposta(b'')
      #   self.send_response(200)
      #   self.send_header('content-type','text/html')
      #   self.end_headers()
      #   self.wfile.write(self.path.encode())