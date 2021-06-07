import socket
import time
import threading

k_recv_s=socket.socket()
k_recv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

s_recv_s=socket.socket()
s_recv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

k_send_s=socket.socket()
k_send_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

s_send_s=socket.socket()
s_send_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

k_recv_port=2024
s_recv_port=2025
k_send_port=2026
s_send_port=2027
ip=""
k_recv_s.bind((ip, k_recv_port))
s_recv_s.bind((ip, s_recv_port))
k_send_s.bind((ip, k_send_port))
s_send_s.bind((ip, s_send_port))

k_recv_s.listen()
s_recv_s.listen()
k_send_s.listen()
s_send_s.listen()

k_recv_session, k_recv_addr = k_recv_s.accept()
s_recv_session, s_recv_addr = s_recv_s.accept()
k_send_session, k_send_addr = k_send_s.accept()
s_send_session, s_send_addr = s_send_s.accept()

def k_recv():
    while True:
        data=k_recv_session.recv(10000000)
        time.sleep(2)
        s_send_session.send(data)

def s_recv():
    while True:
        data=s_recv_session.recv(10000000)
        time.sleep(2)
        k_send_session.send(data)

k1_recv=threading.Thread(target=k_recv)
s1_recv=threading.Thread(target=s_recv)
k1_recv.start()
s1_recv.start()