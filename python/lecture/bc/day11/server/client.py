import socket

def start_client(server_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, 5555))
    while True:
        msg = input("Message: ")
        client.send(msg.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")
        if msg == "quit":
            break
    client.close()

if __name__ == "__main__":
    server_ip = input("Enter server IP: ")  # 서버의 IP 주소를 입력받습니다.
    start_client(server_ip)
