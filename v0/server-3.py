import socket
import time

HEADERSIZE = 10


# Socket object. AF_INET -> IPv4, SOCK_STREAM -> TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Port number is our choice
# s.bind((socket.gethostname(), 1234))
s.bind(("127.0.0.1", 1239))
# Queue of 5
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been extablished")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg

    clientsocket.send(bytes(msg, "utf-8"))
    # clientsocket.close()
    while True:
        time.sleep(3)
        # msg = f"The time is! {time.time()}"
        msg = input("Type something >>")
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        clientsocket.send(bytes(msg, "utf-8"))

