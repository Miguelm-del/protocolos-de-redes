from http.server import HTTPServer, BaseHTTPRequestHandler

PORTA = 8080
HOST = 'localhost'


class cabecalho(BaseHTTPRequestHandler):

    def do_GET(self):
        self.escrever_resposta(b"Hello World")

    def do_POST(self):

        tamanho_dado = int(self.headers.get('content-length', 0))
        corpo = self.rfile.read(tamanho_dado)

        self.escrever_resposta(corpo)

    def escrever_resposta(self, dados):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(dados)

        print(self.headers)
        print("Retorno: ", dados.decode('utf-8'))


print(f"Endereço: http://{HOST}:{PORTA}\n")


servidor = HTTPServer((HOST, PORTA), cabecalho)
servidor.serve_forever()
