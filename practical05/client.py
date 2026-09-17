import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("172.16.160.119", 5000))


while True: 

    reply = input("client: ")
    client.send(reply.encode())
    
    if reply.lower() == "exit":
        break
    
    server_msg=client.recv(1024).decode()
    (print("server:", server_msg))
    
    if reply.lower() == "exit":
        break

client.close()
