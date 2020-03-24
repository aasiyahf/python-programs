from socket import *

serverPort = 12000
closingMessage = 'end trans'
receiving = False

data = ['help', 'me', 'pls']

def main():
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen()
    print 'READY TO WORK'

    while True:
        connectionSocket, addr = serverSocket.accept()
        receiving = True
        sequenceNumber = '0'  # The server's version of ack number
        nextPacketToSend = 0
        while receiving == True:
            i = 0
            if i > 0:
                connectionSocket, addr = serverSocket.accept()
            ACK = connectionSocket.recv(1024)
            print ACK
            if ACK == sequenceNumber:

                connectionSocket.send(data[nextPacketToSend] + sequenceNumber)
                if sequenceNumber == '0':
                    sequenceNumber = '1'
                else:
                    sequenceNumber = '0'

                nextPacketToSend = nextPacketToSend + 1
            elif ACK != sequenceNumber:
                nextPacketToSend = nextPacketToSend - 1

                if sequenceNumber == '0':
                    sequenceNumber = '1'
                else:
                    sequenceNumber = '0'

                connectionSocket.send(data[nextPacketToSend] + ' ' + sequenceNumber)

            i = i + 1

            if ACK == closingMessage:
                connectionSocket.close()
                receiving = False


if __name__ == "__main__":
    main()