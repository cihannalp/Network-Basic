import socket


__author__ = 'cihan'


def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()                 # create socket object
    s.bind((host, port))

    s.listen(1)                         # listen for one client
    connection, address = s.accept()
    print "a client has connected: " + str(address)

    while True:
        data = connection.recv(1024)    # receive data from client (1024 byte buffer)
        print "from client: " + str(data)

        if not data:
            break

        data = str(data).upper()
        print "sending to the client: " + data
        connection.send(data)           # send data to client

    connection.close()

if __name__ == '__main__':
    main()




