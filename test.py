#encoding: utf-8

from socket import *


def handle_request(conn):
    request = conn.recv(1024)
    with open(r'C:\Users\admin\Desktop\django_study\templates\three_day\viewall.html', 'r', encoding='utf-8') as f:
        data = f.read()

    response_head = r'HTTP/1.1 200 OK'
    response = response_head + '\n' + '\n' + data

    conn.send(response.encode())


if __name__ == '__main__':
    socked = socket(AF_INET, SOCK_STREAM)
    socked.bind(('127.0.0.1', 5000))
    socked.listen(5)
    print('等待链接')
    conn, addres = socked.accept()
    print('链接。。。')
    handle_request(conn)


