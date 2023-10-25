import socket
import subprocess

def connect_to_server():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('localhost', 8080))
            break
        except ConnectionRefusedError:
            pass

    while True:
        command = input('Enter a command: ')
        s.sendall(command.encode())

        if command.lower() == 'exit':
            break

    s.close()

if __name__ == '__main__':
    connect_to_server()
