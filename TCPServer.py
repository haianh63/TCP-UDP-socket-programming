import socket

IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 12346

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((IP_ADDRESS, PORT))
ServerSocket.listen(1)  #1 is maximum connection requests from clients
print("The server is ready to receive")
while True:
    connectionSocket, clientAddress = ServerSocket.accept()
    message = connectionSocket.recv(2048).decode('utf-8')
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode('utf-8'))
    connectionSocket.close()