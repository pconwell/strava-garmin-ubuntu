from http.server import BaseHTTPRequestHandler, HTTPServer
import configparser

config = configparser.ConfigParser()
config.read(['./config.ini'])

class S(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(f"Your Auth Token is {self.path.split('=')[2]}".encode('utf-8'))

        config['Authentication']['code'] = self.path.split('=')[2]
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

def run():
    httpd = HTTPServer(('', 8000), S)
    while config['Authentication']['code'] == "":
        httpd.handle_request()
