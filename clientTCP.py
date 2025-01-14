import socket 

HOST = 'localhost'
PORT = 50000

def clientTCP():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(str.encode('CLIENTE TCP - OLÁ'))
    data = s.recv(4096)

    print(f'Mensagem ecoada: {data.decode()}')

if __name__ == "__main__":
    clientTCP()

