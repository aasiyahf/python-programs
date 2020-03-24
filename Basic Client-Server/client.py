from socket import *

serverName = 'localhost'
serverPort = 12000
receiverIsReceiving = False
clientSocket = socket(AF_INET, SOCK_DGRAM)
ACK = '0'
closingMessage = 'end trans'


def main():
    address = (serverName, serverPort)
    clientSocket.bind(address)
    clientSocket.settimeout(2.0)
    receiverIsReceiving = True
    i = 0
    ACK = '0'
    sentence = raw_input("Enter to start")

    while receiverIsReceiving:
        try:
            clientSocket.send(ACK)
            data, addr = clientSocket.recvfrom(1024)
            sequenceNumber = data[-1]
            print data

            if sequenceNumber == ACK:
                if ACK == '0':
                    ACK = '1'
                else:
                    ACK = '0'

                i = i + 1
                if i > 5:
                    receiverIsReceiving = False
                    clientSocket.send(closingMessage)
                    clientSocket.close()
            elif sequenceNumber != ACK:
                clientSocket.send(ACK)
        except timeout:
            print 'timeout here'
            clientSocket.send(ACK)
            print ACK


if __name__ == '__main__':
    main()
