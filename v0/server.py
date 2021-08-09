import socket

print(socket.gethostname())

# Socket object. AF_INET -> IPv4, SOCK_STREAM -> TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Port number is our choice
# s.bind((socket.gethostname(), 1234))
s.bind(("127.0.0.1", 1234))
# Queue of 5
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection fron {address} has been extablished")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
