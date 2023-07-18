import socket 
s= socket.socket()
#reserve a port in yo computer 
port= 12345

#binding the port 
#the plank string on bind is for the ip in this case its the host
s.bind(('',port))
print("socket binded to ...%s" %port)
#onlu five clients allowed to connect
s.listen(5)
print("socket is listening ,,,,,, \n ")
client,addr = s.accept()
      #accept the connection
    # addr is the address of the client that connected
print(f"Connection from {addr} has been established.")
client.send("ssup fucker ".encode())
while True:
   # encode the message sending to trhe client
    message = client.recv(1024).decode()
    print("client :%s"%(message))
    
    if not message:
        break 
    reply = input("Server: ")
    client.send(reply.encode())

s.close()
