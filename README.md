# srget

###### What is this program ######
This is a file downloader program that lets user input file name and resource path in order to download requested file.

###### Language that was used to create this program. ######
Python

###### How to Operate this program. #######
1. Run Terminal in linux or Mac OSX

2. Type "srget -o <output file> -c <numConn> http://someurl.domain[:port]/path/to/file" without quotation in terminal
   where <output file> is your desired filename, <numConn> is your desired number of connection (this will help increase download speed), and  "port" is a port of connection.

3. Press "enter" key on keyboard

###### Library that was used in this program ######
1. asyncore, for multi-connection for increase download speed.
2. cStringIO
3. socket
4. urlparse
5. os
6. sys

