# 作者： 周泳
# 时间： 2022年06月30日16时分55秒
import socket


client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest_addr=('192.168.1.155',2000)
client.sendto('hello'.encode('utf8'),dest_addr)
data = client.recvfrom(100)
print(data.decode('utf8'))
client.close()

