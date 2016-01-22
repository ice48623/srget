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
    data = ''
    # remainder = ''
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
    # header = store_header(sock)[0]
    # remainder = store_header(sock)[1]
    header, remainder = store_header(sock)
    length = Find_Length(header)
    
    body_data = remainder
    while True:
        if len(body_data) == length:
            return body_data

        body_data += sock.recv(1024)
    

print body(sock)




