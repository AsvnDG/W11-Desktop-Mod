import http.server
import socketserver

# Specify the port number
PORT = 8000

# Define the request handler
Handler = http.server.SimpleHTTPRequestHandler

# Create and start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()