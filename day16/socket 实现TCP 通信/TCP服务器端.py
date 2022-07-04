# 作者： 周泳
# 时间： 2022年06月30日22时分08秒
from socket import*

tcp_server = socket(AF_INET,SOCK_STREAM)
server_addr = ('192.168.1.155',1999)
tcp_server.bind(server_addr)
tcp_server.listen(10)
client_socket,client_addr = tcp_server.accept()
recv_data = client_socket.recv(100)
print(recv_data)
client_socket.send(b'study')
client_socket.close()
tcp_server.close()