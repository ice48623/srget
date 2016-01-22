#!/usr/bin/python

import socket as sk
from urlparse import urlparse
import os
import sys



# #print "{!r}".format(mkDownloadRequest('intranet.mahidol','/'))
# def takeInput(path):
#     serv = str(sys.argv[1])
#     print serv


def srget():
    def mkDownloadRequest(serv, objName):
        return ("GET {o} HTTP/1.1\r\n"+"Host: {s}"+"\r\n\r\n").format(o=objName, s=servName)
    servName = 'cs.muic.mahidol.ac.th'
    objName = '/courses/ds/hw/a1.pdf'
    port = 80



    # create an empty socket
    sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    # connect to a destination as specified by the pair
    sock.connect((servName, port))

    request = mkDownloadRequest(servName, objName)
    sock.send(request)

    

    def store_header(sock):
        header = ''
        data = ''
        while True:
            data_part = sock.recv(1024)
            data = data + data_part

            if '\r\n\r\n' in data:
                index = data.find('\r\n\r\n')
                header = data[:index+3]
                remainder = data[index+4:]
                return header,remainder

    # print store_header(sock)
    def Find_Length(header):
        # header = store_header(sock)[0]
        start = header.find("Content-Length")
        end = header.find("\r\n\r\n")

        length = header[start:end]
        # print header

        start2 = length.find(":") +2
        end2 = length.find("\r\n")
        length_final = length[start2:end2]
        return int(length_final)

    # print Find_Length(sock)

    def body(sock):
        # header, remainder = store_header(sock)
        # length = Find_Length(header)
        # body_data = remainder
        # while True:
        #     if len(body_data) == length:
        #         body = open('download.pdf', 'a+')
        #         body.write(body_data)
        #         # print os.path.getsize('download.txt')
        #         # return body_data
        #         break

        #     body_data += sock.recv(1024)

        header, remainder = store_header(sock)
        length = Find_Length(header)

        body_data = remainder
        while True:
            if len(body_data) == length:
                print 'enter if'
                body = open('download.pdf', 'a+')
                body.write(body_data)
                # print os.path.getsize('download.txt')
                # return body_data
                break

            body_data += sock.recv(1024)
            # print body_data
            # body = open('download.pdf', 'a+')
            # body.write(body_data)
        
    body(sock)
srget()




