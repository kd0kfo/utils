#!/usr/bin/env python
#
# Basic HTTPS server.
# command line argument 1 must be a .pem certificate
#
# Create a local_http_handler module with a class, MainClass, that 
# handles requests as a BaseHTTPServer.BaseHTTPRequestHandler

import BaseHTTPServer, SimpleHTTPServer
import ssl
from sys import argv

import local_http_handler

PORT_NUMBER = 8443

try:
    server = BaseHTTPServer.HTTPServer(('localhost', PORT_NUMBER), local_http_handler.MainClass)
    server.socket = ssl.wrap_socket (server.socket, certfile=argv[1], server_side=True)
    print('Started httpserver on port %d' % PORT_NUMBER)

    server.serve_forever()

except KeyboardInterrupt:
    print 'Interrupt received, shutting down the web server'
    server.socket.close()
