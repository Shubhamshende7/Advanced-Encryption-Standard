'''***************************************************************************************************
*                   Copyright 2022-2023 CyPro corporation. All rights reserved.
*  THE SOFTWARE AND INFORMATION CONTAINED HEREIN ARE PROPRIETARY AND CONFIDENTIAL. THIS SOFTWARE IS FOR 
*   INTERNAL USE ONLY AND ANY REPRODUCTION TO ANY PARTY OUTSIDE IS IS STRICTLY PROHIBITED. 
*
* @sumary       Socket Connection
* @description  Establish a connection between server and client.
* @version      1.1.1
* @file         server.py
* @author       Shubham Shende, Amit Dehariya
* 
*****************************************************************************************************'''

#---------------------------------------------Imports--------------------------------------------------

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

    
