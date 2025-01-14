import socket 
import threading

HOST = 'localhost'
PORTTCP = 50000
PORTUDP = 50001

def handleTCPclient(clientSocket):
    request = clientSocket.recv(1024)
    print(f'[TCP] Recebido: {request.decode()}')
    clientSocket.send('ACK do servidor TCP'.encode())
    clientSocket.close()

def serverTCP():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORTTCP))
    server.listen(5)

    print('[TCP] Servidor está escutando...')

    while True:
        client, addr = server.accept()
        print(f'[TCP] Conexão aceita: {addr[0]}:{addr[1]}')
        cliente_handler = threading.Thread(target=handleTCPclient, args=(client,))
        cliente_handler.start()

def handleUDPclient(data, addr, serverSocket):
    print(f'[UDP] Recebido: {data.decode()} from {addr}')
    serverSocket.sendto('ACK do servidor UDP'.encode(), addr)

def serverUDP():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORTUDP))

    print('[UDP] Servidor está escutando...')

    while True:
        data, addr = server.recvfrom(1024)
        clientHandler = threading.Thread(target=handleUDPclient,args=(data,addr,server))
        clientHandler.start()

def main():
    serverTCPThread = threading.Thread(target=serverTCP)
    serverUDPThread = threading.Thread(target=serverUDP)

    serverTCPThread.start()
    serverUDPThread.start()
    serverTCPThread.join()
    serverUDPThread.join()

if __name__ == "__main__":
    main()