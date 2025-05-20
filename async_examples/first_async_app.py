import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ("127.0.0.1", 8000)
server_socket.bind(address)

server_socket.listen()
connection, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established!")