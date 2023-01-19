# Pavlo Yatluk
# dz 15.
# 1. До завд. 11  до серверу чату додати систему логування рівня INFO, WARNING and ERROR.


import logging
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 60000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    logging.basicConfig(level=logging.INFO, filename='d_15.log', filemode='a',
                        format='%(name)s - %(levelname)s - %(asctime)s - %(message)s')
    logging.warning(f"'connected:', {addr}")
    print('connected:', addr)
    data = conn.recv(1024)
    logging.info(f"'Data:', {data}")
    print(str(data))
    if data == bytes("Hello!", encoding='UTF-8'):
        conn.send(bytes("Hi!", encoding='UTF-8'))
    elif data == bytes("Goodbye!", encoding='UTF-8'):
        conn.send(bytes("Bye!", encoding='UTF-8'))
    else:
        conn.send(bytes("I don't understand!", encoding='UTF-8'))
        logging.error('I do not understand!')
conn.close()
