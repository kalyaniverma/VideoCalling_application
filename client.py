import cv2
import socket
import base64
import os
import time
import threading

def videoreciver():
    s=socket.socket()
    ip="13.234.111.201"
    port=2026
    s.connect((ip,port))
    i=0
    while True:
        time.sleep(0.2)
        try:
            data =s.recv(100000000)
            #print(data)
            imgdata = base64.b64decode(data)
            filename="{}.jpg".format(i)
            with open(filename, 'wb') as f:
                f.write(imgdata)

            image= "image"+"{}".format(i)
            image=cv2.imread(filename)

            print(image)
            cv2.imshow('Friend calling...',image)
            os.remove("{}.jpg".format(i))
            i=i+1
            if cv2.waitKey(100) == 13:
                break

        except:
            pass
    cv2.destroyAllWindows()

def videosender():
    #sending video
    s=socket.socket()
    ip="13.234.111.201"
    port=2024
    s.connect((ip,port))
    cap=cv2.VideoCapture(0)
    while True:
        time.sleep(0.2)
        ret,photo=cap.read()
        cv2.imwrite("videocall.jpg",photo)
        with open("videocall.jpg", 'rb') as f:
            image_encoded=base64.b64encode(f.read())
        s.send(image_encoded)

t_recv=threading.Thread(target=videoreciver)
t_send=threading.Thread(target=videosender)
t_recv.start()
t_send.start()