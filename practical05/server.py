import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("172.16.160.119", 5000))
server.listen(1)

print("Server is listening")

conn, addr = server.accept()
print("Server is ready to accept:", addr)

while True:
    client_msg = conn.recv(1024).decode()
    print("client:", client_msg)

    if client_msg.lower() == "exit":
        break

    reply = input("server: ")
    conn.send(reply.encode())

    if reply.lower() == "exit":
        break

conn.close()
server.close()
