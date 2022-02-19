from http.server import HTTPServer, BaseHTTPRequestHandler
#Importação das clases da biblioteca http.server, que nos ajudara a criar nosso web server HTTP
#https://docs.python.org/3/library/http.server.html

HOST = 'localhost' #Endereço
PORT = 8596 # Porta do servidor

#$ curl localhost:8596 -d “Olá Mundo” 


# class http.server.BaseHTTPRequestHandler( request , client_address , server ) 
# Essa classe é usada para lidar com as solicitações HTTP que chegam ao servidor. Por si só, ele não pode responder a nenhuma solicitação HTTP real; ele deve ser subclassificado para lidar com cada método de solicitação (por exemplo, GET ou POST). BaseHTTPRequestHandlerfornece um número de variáveis ​​de classe e instância e métodos para uso por subclasses.

# O manipulador analisará a solicitação e os cabeçalhos e chamará um método específico para o tipo de solicitação. O nome do método é construído a partir da solicitação. Por exemplo, para o método de solicitação SPAM, o do_SPAM() método será chamado sem argumentos. Todas as informações relevantes são armazenadas em variáveis ​​de instância do manipulador. As subclasses não devem precisar substituir ou estender o __init__()método.

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.write_response(b'')

    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length)
        #Mensagem em bytes

        self.write_response(body)

    def write_response(self, content):
        self.send_response(200) #Mostrar que esta ok 
        self.end_headers()
        self.wfile.write(content)
        print(self.headers)
        print("Retorno:")
        print(content.decode('utf-8')) #Transformar em string



print(f'Listening on http://{HOST}:{PORT}\n')

httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()




# class http.server.HTTPServer( server_address , RequestHandlerClass ) 
# Essa classe se baseia na TCPServerclasse armazenando o endereço do servidor como variáveis ​​de instância chamadas server_namee server_port. O servidor é acessível pelo manipulador, normalmente por meio da servervariável de instância do manipulador.