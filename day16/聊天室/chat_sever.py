# 作者： 周泳
# 时间： 2022年07月03日14时分33秒
from socket import*

tcp_server = socket(AF_INET,SOCK_STREAM)
server_addr =('192.168.1.155',2000)
tcp_server.bind(server_addr)
tcp_server.listen(10)
client_socket,client_addr = tcp_server.accept()
while True:
    recv_data = client_socket.recv(100)
    print(recv_data)
    data = input('server请输入:')
    client_socket.send(data.encode('utf8'))
    client_socket.close()
    tcp_server.close()
