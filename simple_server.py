import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET for ipv4, SOCK_DGRAM for UDP abstraction
server.bind(('', 12000))

while True:
    bytes_message, ip_client_address = server.recvfrom(2048)
    response_message = bytes_message.decode().upper()
    server.sendto(response_message.encode(), ip_client_address)
    print(response_message)
