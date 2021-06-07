# VideoCalling_application

Here are two files, sever.py and client.py
server.py file is launched in AWS Instance and maximum 2 people can connect to this server at a time. This code will receive the video of one client and send it to other, it will be done both ways in parallel.
client.py file is launched in local system and has the responsibility to go to server and build a connection so that client's side video will be received by the server and the video forwarded by server will be received by the client. Same goes for the other client too.
And client.py should be run by both the clients who are communicating, at the same time.

**Concepts Used:-**
OpenCV
Sokcet Programming
Threading
