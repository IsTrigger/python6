# 作者： 周泳
# 时间： 2022年06月30日22时分21秒
from socket import *

tcp_client = socket(AF_INET,SOCK_STREAM)
dest_addr = ('192.168.1.155',1999)
tcp_client.connect(dest_addr)
tcp_client.send(b'python6')
data = tcp_client.recv(100)
print(data)
tcp_client.close()