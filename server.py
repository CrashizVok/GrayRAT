import socket
import threading

# Set up the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(5)
    print('Server is listening...')

    while True:
        client, addr = server.accept()
        print('Client connected:', addr)

        # Create a new thread for the connection
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

def handle_client(client):
    while True:
        data = client.recv(1024)
        if not data:
            break

        print('Received:', data)

if __name__ == '__main__':
    start_server()
