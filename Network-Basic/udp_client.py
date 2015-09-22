import socket


__author__ = 'cihan'


def main():

    server = ('127.0.0.1', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = raw_input("> ")

    while message != "q":
        s.sendto(message, server)
        print "Connected to: " + str(server)
        print "Send to server: " + str(message)

        data, address = s.recvfrom(1024)
        print "Received from server: " + str(data)
        message = raw_input("> ")

    s.close()

if __name__ == '__main__':
    main()
