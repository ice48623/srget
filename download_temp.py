import socket as sk
from urlparse import urlparse
import os

def mkDownloadRequest(serv, objName):
    return ("GET {o} HTTP/1.1\r\n"+"Host: {s}"+"\r\n\r\n").format(o=objName, s=servName)

# #print "{!r}".format(mkDownloadRequest('intranet.mahidol','/'))
servName = 'intranet.mahidol'
# objName = '/courses/ds/hw/a1.pdf'
port = 80

# create an empty socket
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
# connect to a destination as specified by the pair
sock.connect((servName, port))

request = mkDownloadRequest(servName, '/')
sock.send(request)

# # create an empty socket
# sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
# # connect to a destination as specified by the pair
# sock.connect((servName, port))
#
# request = mkDownloadRequest(servName, '/')
# sock.send(request)
#
# if not os.path.exists('./download'):
#     collector = open('download', 'w+').close()
# collector = open('download', 'a+')
# while True:
#     data = sock.recv(1024)
#     print data
#     end_header = data.find("\r\n\r\n")
#     print end_header
#
#     if end_header != 0:
#         print 'end-header founded'
#         if os.path.exists('./download'):
#             print "enter if"
#             with open('download', 'a+') as collector:
#
#                 collector.write(data[:end_header])
#                 print collector.read()
#     # with open('download', 'a+') as collector:
#     #     collector.write(data)
#     collector.write(data)
#
# collector.close()

def store_header(sock):

    # if not os.path.exists('./length.txt'):
    #     collector = open('length.txt', 'w+')
    #     collector.close()
    header = ''
    remainder = ''
    while True:
        data = sock.recv(1024)
        header = header + data

        if '\r\n\r\n' in header:
            index = header.find('\r\n\r\n')
            header = header[:index+3]
            remainder = header[index:]
            return header,remainder

def Find_Length(sock):
    header = store_header(sock)[0]
    start = header.find("Content-Length")
    end = header.find("\r\n\r\n")

    length = header[start:end]
    # print header

    start = length.find(":") +2
    end = length.find("\r\n")
    length = length[start:end]
    return length

# print Find_Length(sock)

def body(sock):
    header = store_header(sock)[1]
    length = Find_Length(sock)
    print header
    print length

print body(sock)




