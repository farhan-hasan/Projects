import socket

HEADER = 64
PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    msg = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)
    print(client.recv(1024).decode(FORMAT))

username = input("Enter your username: ")
client.send(username.encode(FORMAT))
print(client.recv(2048).decode(FORMAT))
print(client.recv(2048).decode(FORMAT))
while True:
    message = input(f"[Client] Send message: ")
    if message == DISCONNECT_MESSAGE:
        send(message)
        print(f"[Client] Connection closed")
        break
    send(message)