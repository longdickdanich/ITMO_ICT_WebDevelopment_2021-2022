import socket
from threading import Thread

def send():
    while True:
        message = input()
        conn.send(message.encode('utf-8'))


def get():
    while True:
        data = conn.recv(1024).decode('utf-8')
        print(data)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('127.0.0.1', 65432))
Thread(target=send).start()
Thread(target=get).start()