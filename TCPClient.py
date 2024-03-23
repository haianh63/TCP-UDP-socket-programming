import socket
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 12346

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSocket.connect((IP_ADDRESS, PORT))
message = input("Input lowercase sentence: ")
ClientSocket.send(message.encode('utf-8'))
modifiedMessage = ClientSocket.recv(2048)
print(f"Modified message: {modifiedMessage.decode('utf-8')}")
ClientSocket.close()