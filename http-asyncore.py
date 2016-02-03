#!usr/bin/env python
import asyncore, socket
import logging
from cStringIO import StringIO ## StringIO append is faster than the normal one


def make_request(req_type, what, details, version="1.1"):
    """ Compose an HTTP request """
    NL = "\r\n"
    request_line = "{req_type} {what} HTTP/{ver}".format(
        req_type=req_type,
        what=what,
        ver=version
    )
 
    detail_lines = NL.join(
        "{}: {}".format(name, value) for name, value in details.iteritems()
    )
 
    full_request = request_line + NL + detail_lines + NL + NL
    return full_request


# print make_request("GET", "/", {"Host": "me.com"})

class HTTPClient(asyncore.dispatcher): ## inherit - extend in python style

	def __init__(self, host, path):
		asyncore.dispatcher.__init__(self)	## super -- call structure of super class , self is itself object
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect((host, 80))

		self.host = host

		self.recvbuf = StringIO()  ## it's like string builder
		self.logger = logging.getLogger(host+path)

		self.sendbuf = ""
		## make my request
		self.write(
			make_request('GET', path,
				{"host": host, "Connection": "close"}) ## Non-persistent connection
			)

	def write(self, msg):
		self.sendbuf += msg


	def handle_connect(self):
		self.logger.debug("connection established")


	def handle_close(self):
		self.logger.debug("got disconnected")
		self.close()


	def handle_read(self): ## when recv = there is something for you to read --> do what
		buf = self.recv(8192) ## 2K - 10K -- recoomend 8K
		self.recvbuf.write(buf)
		self.logger.debug("recv {0} bytes".format(len(buf)))


	def writeable(self): # if there is anything to send??
		return len(self.sendbuf) > 0 ## you have sth to send


	def handle_write(self):
		bytes_send = self.send(self.sendbuf)
		self.sendbuf = self.sendbuf[bytes_send:] ## the remainder


clients = [ ## simultineously download
	HTTPClient("www.nytimes.com", "/") ,
	HTTPClient("www.chula.ac.th", "/") ,
# 	HTTPClient("www.cnn.com", "/") ,
# 	HTTPClient("www.wsj.com", "/")
]
# HTTPClient("www.nytimes.com", "/")

logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)-15s %(name)s: %(message)s"
    )
 
asyncore.loop()
