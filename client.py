import socket 

client= socket.socket()
port = int(input("enter the port number to listen to :"))

host= input("enter the host to connect to : " )

client.connect((host,port))
while True:
    # Receive and print messages from the server
    msg = client.recv(1024).decode()
    print("\nServer:", msg)

    if msg.lower() == "exit":
        break

    # Send a message to the server
    message = input("client : ")
    client.send(message.encode())