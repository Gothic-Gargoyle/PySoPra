# Name: Board games server
# version: 0.1POC
# Description: I want to see if i can make battleships in Python and build
# a server for it ánd other boardgames

import socket
NAME = "BGServer"
HOST = '127.0.0.1'
PORT = 1648

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"{NAME} listening on {PORT}")
    conn,addr = s.accept()
    with conn:
        print(f"connected by {addr}")
        conn.send(f"Hello, welcome to {NAME}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)