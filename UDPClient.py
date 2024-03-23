import socket

IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 12345
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Input lowercase sentence: ")
ClientSocket.sendto(message.encode('utf-8'), (IP_ADDRESS, PORT))
modifiedMessage, serverAddress = ClientSocket.recvfrom(2048)
print(f"Modified message: {modifiedMessage.decode('utf-8')}")
ClientSocket.close()