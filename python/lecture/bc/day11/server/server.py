import socket
import threading


def handle_client(client_socket, address):
    print(f"Connection from {address} has been established.")
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf-8")
            if msg:
                print(f"{address}: {msg}")
                # 여기서 게임 로직 처리
                response = "Message received"
                client_socket.send(response.encode("utf-8"))
            else:
                break
        except ConnectionResetError:
            break
    print(f"Connection with {address} closed.")
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))  # 모든 인터페이스에서 접근 가능하게 합니다.
    server.listen()
    print("Server is listening on port 5555...")
    while True:
        client, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    start_server()
