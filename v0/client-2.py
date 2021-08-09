import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This is client so connecting to server, instead of binding
# s.connnect((socket.gethostname(), 1234))
s.connect(("127.0.0.1", 1239))

# the below number denotes buffer size. Bigger the message, bigger should be the buffer
while True:
    full_msg = ""
    new_msg = True
    while True:
        msg = s.recv(1024)
        if new_msg:
            # print(f"new mwssage length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msglen:
            # print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ""
    print(full_msg)

