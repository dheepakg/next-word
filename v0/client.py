import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This is client so connecting to server, instead of binding
# s.connnect((socket.gethostname(), 1234))
s.connect(("127.0.0.1", 1234))

# the below number denotes buffer size. Bigger the message, bigger should be the buffer

while True:
    msg = s.recv(1024)

    print(msg.decode("utf-8"))

