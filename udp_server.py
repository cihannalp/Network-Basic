import socket


__author__ = 'cihan'


def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create socket object
    s.bind((host, port))
    print "Server Created"

    while True:
        data, address = s.recvfrom(1024)                  # receive data from client
        print "connected to: " + str(address)
        print "from connected user: " + str(data)

        data = str(data).upper()
        s.sendto(data, address)                           # send data to client
        print "send to connected user: " + str(data)

    s.close()


if __name__ == '__main__':
    main()