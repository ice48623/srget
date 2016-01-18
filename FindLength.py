import socket as sck

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
        data = sock.recv(10000)
        #print "{!r}".format(data)
        #print data
        ## Find where is the "Content-Length" and the end of it
        ctl_start = data.find("Content-Length")
        ctl_end = data.find("\r\n\r\n")
        body_start = data.find("\r\n\r\n")
        body_end = data.find("</HTML>")

        ## Slice data variable and store only "Content-Length" line
        Content_Length = data[ctl_start:ctl_end]
        #print "Content_Length 1: ", Content_Length
        ## Update ctl_start to the new index
        ctl_start = Content_Length.find(":") + 1
        ctl_end = Content_Length.find("\r\n")
        #print "Content_Length1 =",  Content_Length
        Content_Length = Content_Length[ctl_start:ctl_end+1]
        Content_Length = Content_Length.strip()
        Content_Length = int(Content_Length)
        print "Content_Length =",  Content_Length
        #print data
        data = data[body_start:body_end]
        #data = data.strip()

        print "{!r}.format(data)
        print "len(data)", len(data)

        #sock.close
        #break
        if Content_Length == len(data):
            sock.close()
            return Content_Length
            #break


print FindLength()
