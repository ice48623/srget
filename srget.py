import socket as sck
import os

def mkDownloadRequest(serv, objName):
    return ("GET {o} HTTP/1.1\r\n"+"Host: {s}"+"\r\n\r\n").format(o=objName, s=servName)

servName = 'cs.muic.mahidol.ac.th'
objName = '/courses/ds/hw/a1.pdf'
port = 80
#print "{!r}".format(mkDownloadRequest('www.google.com','/'))
def FindLength():

    # create an empty socket
    sock = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    # connect to a destination as specified by the pair
    sock.connect((servName, port))

    request = mkDownloadRequest(servName, objName)
    sock.send(request)

    while True:
        data = sock.recv(1024)
        #print "{!r}".format(data)
        # print data
        if os.path.exists('./temp.pdf'):
            print "enter if"
            with open('temp.pdf', 'a+') as collector:
                collector.write(data)
                print collector.read()
        else:
            print 'not found'
            collector = open('temp.pdf', 'w+').close()


        # sock.close
        # break


print FindLength()
