import socket

if __name__ == "__main__":
    ip = "192.168.30.10"
    port = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))

    server.listen(10)

    while True:
        client, address = server.accept()
        print(f"Connection Established: {address[0]}:{address[1]}")

        client.send(bytes("Who are you?", "utf-8"))
        
        data = client.recv(1024)
        data = data.decode("utf-8")
        print(data)

        client.close()

    
