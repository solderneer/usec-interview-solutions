#!/usr/bin/env python3

import socket, sys
from struct import *

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    count = 0

    while True:
        packet = sock.recvfrom(65565) # maximum size
        packet = packet[0] # Take first one out of tuple
        ip_header = packet[0:20]

        lenth, src_addr, dest_addr = unpack_ip(ip_header)
        src_port, dest_port = unpack_tcp(packet[lenth:lenth+20])

        print('Packet number: ' + str(count))
        print('Source Address: ' + str(src_addr) + ' Source port: ' + str(src_port))
        print('Destination Address: ' + str(dest_addr) + ' Destination port: ' + str(dest_port))

        count += 1

def unpack_ip(data):
    ip_header = unpack('!BBHHHBBH4s4s', data)
    length = (ip_header[0] & 0xF) * 4 # Calculating length of header using a mask to find IHL
    src_addr = socket.inet_ntoa(ip_header[8])
    dest_addr = socket.inet_ntoa(ip_header[9])

    return (length, src_addr, dest_addr)

def unpack_tcp(data):
    tcp_header = unpack('!HHLLBBHHH', data)
    src_port = tcp_header[0]
    dest_port = tcp_header[1]

    return (src_port, dest_port)

main()
