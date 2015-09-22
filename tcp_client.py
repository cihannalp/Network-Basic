import socket


__author__ = 'cihan'


def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()         # create a socket object
    s.connect((host, port))     # connect to given host and port
    print "Connected to server"

    message = raw_input("> ")
    while message != 'q':
        s.send(message)         # send data to server
        data = s.recv(1024)     # receive data from server (1024 byte buffer)
        print "Received from server: " + str(data)
        message = raw_input("> ")
    s.close()

if __name__ == '__main__':
    main()
