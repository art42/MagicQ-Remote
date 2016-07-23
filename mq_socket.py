############################################################################
##  MagicQ Socket Session
##  July 21, 2016
##  Austin Tyler
##
##  Reference: MagicQ Manual - Chapter 31. ChamSys Remote Protocol Commands
##             http://chamsys.co.uk
############################################################################

import socket

class mq_remote(socket.socket):

    INADDR_ANY = "" # INADDR_ANY
    INADDR_BROADCAST = "<broadcast>" # INADDR_BROADCAST
    MQ_DEFAULT_PORT = 6553

    def __init__(self, ip = INADDR_ANY, port = MQ_DEFAULT_PORT):
        'initialize a socket to take to a remote MagicQ instance'
        socket.socket.__init__(self, socket.AF_INET, socket.SOCK_DGRAM)

        # Declare Instance Variables
        self.MAGICQ_IP = ip
        self.PORT = port

        # config the MagicQ socket options
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind to remote MagicQ port
        self.bind((ip, port))

        if ip == mq_remote.INADDR_ANY:
            # Set to broadcast mode
            self.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        ## If Windows
        # s.ioctl(socket.FIONBIO, 1)

    def tx(self, msg):
        'send MagicQ command'
        if self.MAGICQ_IP != mq_remote.INADDR_ANY:
            self.sendto(msg, (self.MAGICQ_IP, self.PORT))
        else:
            self.sendto(msg, (mq_remote.INADDR_BROADCAST, self.PORT))

    def rx(self):
        'receive MagicQ command'
        print(self.recv(128))
