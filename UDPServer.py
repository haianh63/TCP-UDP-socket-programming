import socket

IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 12345
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerSocket.bind((IP_ADDRESS, PORT))

print("The server is ready to receive")
while True:
    message, clientAddress = ServerSocket.recvfrom(2048)
    modifiedMessage = message.decode('utf-8').upper()
    ServerSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)