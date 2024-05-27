from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the request URL
        parsed_url = urlparse(self.path)
        # Parse query parameters
        query_params = parse_qs(parsed_url.query)

        # Check if 'operation', 'num1', and 'num2' are present in the query parameters
        if 'operation' in query_params and 'num1' in query_params and 'num2' in query_params:
            operation = query_params['operation'][0]
            num1 = float(query_params['num1'][0])
            num2 = float(query_params['num2'][0])

            # Perform the requested operation
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Cannot divide by zero"
            else:
                result = "Invalid operation"
        else:
            result = "Missing parameters"

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

