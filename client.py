'''***************************************************************************************************
*                   Copyright 2022-2023 CyPro corporation. All rights reserved.
*  THE SOFTWARE AND INFORMATION CONTAINED HEREIN ARE PROPRIETARY AND CONFIDENTIAL. THIS SOFTWARE IS FOR 
*   INTERNAL USE ONLY AND ANY REPRODUCTION TO ANY PARTY OUTSIDE IS IS STRICTLY PROHIBITED. 
*
* @sumary       Socket Connection
* @description  Establish a connection between server and client.
* @version      1.1.1
* @file         client.py
* @author       Shubham Shende, Amit Dehariya
* 
*****************************************************************************************************'''

#---------------------------------------------Imports--------------------------------------------------

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

    
