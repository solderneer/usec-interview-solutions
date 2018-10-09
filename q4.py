#!/usr/bin/env python3

import socket
import sys

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 3111

CLIENT_HOST = '127.0.0.1'
CLIENT_PORT = 2999

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock = socket.socket(socket.AF_INET, socker.SOCK_STREAM)
print('Sockets created')

client_sock.connect((CLIENT_HOST, CLIENT_PORT))
print('Client socket connected')

server_sock.bind((SERVER_HOST, SERVER_PORT))
print('Server socket bound')

server_sock.listen(1) # Only allow one backlog connection before refusing
print('Server is listening on port ' + SERVER_PORT)

conn, addr = server_sock.accept()

with conn:
    print('Connected to ' + addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        client_sock.sendall(data)
        data = client_sock.recv(1024)
        conn.sendall(data)
        
