import socket as sk
from urlparse import urlparse
import os

def mkDownloadRequest(serv, objName):
    return ("GET {o} HTTP/1.1\r\n"+"Host: {s}"+"\r\n\r\n").format(o=objName, s=servName)

# #print "{!r}".format(mkDownloadRequest('intranet.mahidol','/'))
servName = 'intranet.mahidol'
# objName = '/courses/ds/hw/a1.pdf'
port = 80
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

def Find_Length():
    # create an empty socket
    sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    # connect to a destination as specified by the pair
    sock.connect((servName, port))

    request = mkDownloadRequest(servName, '/')
    sock.send(request)
    ContentLength = 0
    # if not os.path.exists('./length.txt'):
    #     collector = open('length.txt', 'w+')
    #     collector.close()
    collector = open('length.txt', 'a+')
    print os.path.getsize('./length.txt')
    while True:
        data = sock.recv(1024)
        print data
        # collector = open('length.txt', 'a+')
        collector.write(data)
        # print data
        for line in collector:
            # print line
            ContentLength = line.find("Content-Length:")
            if ContentLength != -1:
                sock.close
                collector.close()
                return ContentLength
        # collector.close()
print Find_Length()