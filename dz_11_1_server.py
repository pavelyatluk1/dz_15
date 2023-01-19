import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 60000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    if data == bytes("Hello!", encoding='UTF-8'):
        conn.send(bytes("Hi!", encoding='UTF-8'))
    elif data == bytes("Goodbye!", encoding='UTF-8'):
        conn.send(bytes("Bye!", encoding='UTF-8'))
    else:
        conn.send(bytes("I don't understand!", encoding='UTF-8'))
conn.close()
