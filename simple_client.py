import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    send_message = input("Type the message:")
    client.sendto(send_message.encode(), ("127.28.129.76", 12000))
    response_bytes, ip_server_address = client.recvfrom(2048)
    print(response_bytes.decode())
