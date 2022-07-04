# 作者： 周泳
# 时间： 2022年06月30日16时分13秒
from socket import *

udp_server = socket(AF_INET,SOCK_DGRAM)
local_adrr=('192.168.1.155',2000)
udp_server.bind(local_adrr)

recv_data = udp_server.recvfrom(1024)
print(recv_data[0].decode('utf8'))
print(recv_data[1])
udp_server.close()