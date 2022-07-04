# 作者： 周泳
# 时间： 2022年07月03日14时分18秒
from socket import *

tcp_client = socket (AF_INET,SOCK_STREAM)
dest_addr = ('192.168.1.155',2000)
tcp_client.connect(dest_addr)
while True:
    data = tcp_client.recv(100)
    print(data.decode('utf8'))
    data = input('client请输入：')
    tcp_client.send(data.encode('utf8'))
tcp_client.close()