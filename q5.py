#!/usr/bin/env python3

import socket

def main():
    sock = socket.socket(socket.AF_NET, socket.SOCK_RAW, socket.ntohs(3))
    count = 0

    while True:
        packet = sock.recvfrom(65565) # maximum size
        packet = packet[0] # Take first one out of tuple
        ip_header = packet[0:20]

        lenth, src_addr, dest_addr = unpack_ip(ip_header)
        src_port, dest_port = unpack_tcp(packet[lenth:lenth+20])

        print('Packet number: ' + str(count))
        print('Source Address: ' + str(src_address) + ' Source port: ' + str(src_port))
        print('Destination Address: ' + str(dest_address) + ' Destination port: ' + str(dest_port))




def unpack_ip(data):
    ip_header = unpack('!BBHHHBBH4s4s', data)
    length = (ip_header[0] & 0xF) * 4 # Calculating length of header using a mask to find IHL
    src_addr = ip_header[8]
    dest_addr = ip_header[9]

    return (length, src_addr, dest_addr)

def unpack_tcp(data):
    tcp_header = unpack('!HHLLBBHHH', data)
    src_port = tcp_header[0]
    dest_port = tcp_header[1]

    return (src_port, dest_port)
