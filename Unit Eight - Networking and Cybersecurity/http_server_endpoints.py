from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the request URL
        parsed_url = urlparse(self.path)
        # Parse query parameters
        query_params = parse_qs(parsed_url.query)
        url_path = parsed_url.path
        
        if url_path == '/counter':
            result = 0
            if 'str' in query_params:
                sentence = query_params['str'][0]
                numSpaces = 0
                for ch in sentence:
                    if ch == ' ':
                        numSpaces +=1
                result = numSpaces + 1

        elif url_path == '/temperature':
            result = 0
            if 'temp' in query_params:
                temp = int(query_params['temp'][0])
                to = query_params['to'][0]
                if to == 'farenheit':
                    result = temp * (9 / 5) + 32
                else:
                    result = (temp - 32) * (5 / 9)
            elif url_path == '/random':
                result = 'Random Number Generator'
        else:
            result = 'Invalid Path'


        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Send response content
        self.wfile.write(str(result).encode('utf-8'))

# Define the server address and port
server_address = ('', 8080)

# Create an HTTP server with the defined request handler
httpd = HTTPServer(server_address, RequestHandler)

# Start the HTTP server
print('Starting server...')
httpd.serve_forever()

