import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
# sock.setblocking(False)
# sock.settimeout(5)
conn, address = sock.accept()
print(address)

while True:
    data = conn.recv(1024)
    if not data:
        break
    if data.decode("utf8") == "exit":
        conn.send(data)
        break
    else:
        conn.send(data)
        print("[КЛИЕНТ]: "+data.decode())

conn.close()