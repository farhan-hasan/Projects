import socket
import threading

HEADER = 64
PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr, user):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                conn.send(f"[SERVER] Bye {user}".encode(FORMAT))
                print(f"{user} Disconnected")
                connected = False
            print(f"{user}: {msg}")
            conn.send("[SERVER] Message Received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Sever is listening on {IP}")
    while True:
        conn, addr = server.accept()
        username = conn.recv(2048).decode()
        conn.send(f"[SERVER] Welcome {username}".encode(FORMAT))
        conn.send(f"[SERVER] Type -!DISCONNECT- to disconnect from server without dashes".encode(FORMAT))
        thread = threading.Thread(target=handle_client, args = (conn, addr, username))
        thread.start()
        print(f"[ACTIVE CONECTIONS]{threading.active_count() - 1}")

print("[STARTINTG] server is starting...")
start()
