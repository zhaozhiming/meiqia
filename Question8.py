# 编写一个socket程序，守候在900端口，对所有收到的数据原样返回。

import socket
import sys


def socket_server(host='localhost', port=900):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    s.listen(10)

    while 1:
        conn, addr = s.accept()
        buf = conn.recv(64)
        if len(buf) > 0:
            print buf

    s.close()

if __name__ == '__main__':
    socket_server()
