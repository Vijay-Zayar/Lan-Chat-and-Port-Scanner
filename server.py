# Import required modules
import socket
import threading
from tkinter import messagebox

HOST = ''
PORT = 1234  # You can use any port between 0 to 65535
LISTENER_LIMIT = 30
active_clients = []  # List of all currently connected users

# Function to listen for upcoming messages from a client


def listen_for_messages(client, username,address):

    while 1:
        try:
            message = client.recv(2048).decode('utf-8')

            if (not message):
                message = ''
                break   # Client disconnected gracefully

            if message == 'LEAVE':    
                # Notify other clients that this user is leaving
                leave_message = "SERVER~" + f"{username} on {address[0]} has left the chat"
                send_messages_to_all(leave_message)

                # Remove the leaving client from the list of active clients
                try:    
                    active_clients.remove((username, client, address))
                    
                except:
                    print("Error removing client from active list")
                # Close the client socket
                client.close()
                break
            
            # Handle other messages
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)

        except ConnectionResetError:
            # Handle the case where the client disconnects abruptly
            # Remove the client from the list of active clients
            active_clients.remove((username, client,address))

            # Close the client socket
            client.close()
            break   

        

# Function to send message to a single client
def send_message_to_client(client, message):

    client.sendall(message.encode())

# Function to send any new message to all the clients that
# are currently connected to this server


def send_messages_to_all(message):
    # if (type(message) == list):
    #     for user in active_clients:
    #         for msg in message:
    #             send_message_to_client(user[1], message[msg])
    # else:
    for client in active_clients:

        # client[1].sendall(message.encode())
        send_message_to_client(client[1], message)


# Function to handle client

def client_handler(client,address):

    # Server will listen for client message that will
    # Contain the username
    while 1:
        # msg = ['a,b,c']
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            # msg[0] = prompt_message
            send_messages_to_all(prompt_message)
            # messagebox.showinfo("Added",f"{active_clients}")

            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages,
                     args=(client, username,address, )).start()


# Get Local IP Address

def get_local_ip():
    # Get the local IP address of the machine
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


# Main function

def main():
    # Getting Local IP Address
    local_ip = get_local_ip()
    HOST = local_ip

    # Creating the socket class object
    # AF_INET: we are going to use IPv4 addresses
    # SOCK_STREAM: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try catch block
    try:
        # Provide the server with Local IP address in the form of
        # host IP and port
        server.bind((HOST, PORT))
        messagebox.showinfo("Success", f"Server is Running on host: {HOST}")
        print(f"Running the server on {HOST} {PORT}")
    except:
        messagebox.showerror("Failed", "Server is failed to bind")
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # Set server limit
    server.listen(LISTENER_LIMIT)

    # This while loop will keep listening to client connections
    while 1:

        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")
        
        threading.Thread(target=client_handler, args=(client,address, )).start()
        




if __name__ == '__main__':
    main()
