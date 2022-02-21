from http.server import HTTPServer, BaseHTTPRequestHandler

#Importação de metodos da biblioteca http.server


class ecoHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) #Servidor ok
        self.send_header('cottent-type','text/html')
        self.end_headers()
        mensage = input('Digite a mensagem: ')
        self.wfile.write(mensage.encode()) # strings para nytes
        
        







def main(): #Função main
    PORT = 44444
    servidor = HTTPServer(('',PORT), ecoHandler)
    print("Servidor rodando na porta %s" %PORT)
    servidor.serve_forever() #Servidor só será encerrado, quando utilizar ctrl + c no terminal
    

if __name__ == '__main__':
    main()