import socket

if __name__ == "__main__":
    ip = "192.168.30.10"
    port = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))
    
    data = client.recv(1024)
    data = data.decode("utf-8")
    print(data)

    string = input()
    client.send(bytes(string, "utf-8"))

    
