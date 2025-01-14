import socket

def clientUDP():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto('CLIENTE UDP - OLÁ'.encode(), ('localhost', 50001))
    data, addr = client.recvfrom(4096)
    print(f'Mensagem ecodada: {data.decode()}')

if __name__ == "__main__":
    clientUDP()