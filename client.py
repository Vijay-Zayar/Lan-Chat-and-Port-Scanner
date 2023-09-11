# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import datetime

# HOST = ''
PORT = 1234

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 15)
BUTTON_FONT = ("Helvetica", 14)
SMALL_FONT = ("Helvetica", 12)

# Creating a socket object
# AF_INET: we are going to use IPv4 addresses
# SOCK_STREAM: we are using TCP packets for communication
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

def clear_messages():
    message_box.config(state=tk.NORMAL)
    message_box.delete(1.0, tk.END)  # Delete from the start (1.0) to the end (tk.END)
    message_box.config(state=tk.DISABLED)

def leave():

    client.sendall("LEAVE".encode('utf-8'))
    
    # Close the client socket
    # client.close()
    
    # Update the GUI to indicate that the user is leaving
    add_message("[SERVER] You have left the chat")
    # server_ip_textbox.config(state=tk.NORMAL)
    # server_ip_textbox.delete(0, len(server_ip_textbox.get()))
    # server_ip_button.config(state=tk.NORMAL)
    # username_textbox.config(state=tk.NORMAL)
    # username_textbox.delete(0, len(username_textbox.get()))
    # username_button.config(state=tk.NORMAL)
    # clear_messages()
    root.destroy()

def connect():
    # Check username & Host Address are empty or not
    HOST = server_ip_textbox.get()
    username = username_textbox.get()

    if username != '' and HOST != '':

        # try except block for Client Connection
        try:
            # Connect to the server
            client.connect((HOST, PORT))
            print("Successfully connected to server")

            client.sendall(username.encode('utf-8'))

            server_ip_textbox.config(state=tk.DISABLED)
            # server_ip_button.config(state=tk.DISABLED)
            username_textbox.config(state=tk.DISABLED)
            username_button.config(state=tk.DISABLED)

            threading.Thread(target=listen_for_messages_from_server,
                         args=(client, )).start()

            add_message("[SERVER] Successfully connected to the server")
        except:

            messagebox.showerror("Unable to connect to server",
                            f"Unable to connect to server {HOST} {PORT} \n Please check the Server IP Address or Refresh the widow and try again!")
    
    else:
        messagebox.showerror("Invalid Host Address or Username",
                                "Host Address or Username cannot be empty")

        


def send_message():
    message = message_textbox.get()
    if message != '':
        client.sendall(message.encode())
        message_textbox.delete(0, len(message))
    else:
        messagebox.showerror("Empty message", "Your message is empty")


def listen_for_messages_from_server(client):
    try:
        while 1:
            time = datetime.datetime.now().time()
            message = client.recv(2048).decode('utf-8')

            if not message:
                break  # Server closed the connection gracefully

            if message != '':
                username = message.split("~")[0]
                content = message.split('~')[1]

                add_message(f"[{time.hour}:{time.minute}:{time.second}][{username}] {content}")

            else:
                messagebox.showerror(
                    "Error", "Message recevied from client is empty")
    except ConnectionAbortedError:
        # Handle the case where the connection is abruptly closed by the server
        print("Connection to the server was abruptly closed.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Close the client socket when the thread exits
        client.close()

root = tk.Tk()
root.geometry("500x550")
root.title("Messenger Client")
root.resizable(False, False)

# Grid Layout for the widgets

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=3)
root.grid_rowconfigure(3, weight=1)

top_frame = tk.Frame(root, width=500, height=100, bg=DARK_GREY)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle1_frame = tk.Frame(root, width=500, height=100, bg=DARK_GREY)
middle1_frame.grid(row=1, column=0, sticky=tk.NSEW)

middle2_frame = tk.Frame(root, width=500, height=300, bg=MEDIUM_GREY)
middle2_frame.grid(row=2, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, width=500, height=100, bg=DARK_GREY)
bottom_frame.grid(row=3, column=0, sticky=tk.NSEW)

# Enter Server IP Address
server_ip_label = tk.Label(
    top_frame, text="Enter Server IP:", font=FONT, bg=DARK_GREY, fg=WHITE)
server_ip_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

server_ip_textbox = tk.Entry(
    top_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=24)
server_ip_textbox.pack(side=tk.LEFT, pady=5)

server_ip_button = tk.Button(
    top_frame, text="Leave", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=leave)
server_ip_button.pack(side=tk.LEFT, padx=10, pady=5)

# Enter Username
username_label = tk.Label(
    middle1_frame, text="Enter username:", font=FONT, bg=DARK_GREY, fg=WHITE)
username_label.pack(side=tk.LEFT, padx=5, pady=3)

username_textbox = tk.Entry(
    middle1_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=24)
username_textbox.pack(side=tk.LEFT, pady=3)

username_button = tk.Button(
    middle1_frame, text="Join", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=connect)
username_button.pack(side=tk.LEFT, padx=10, pady=5)

# Display Message
message_box = scrolledtext.ScrolledText(
    middle2_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE, width=67, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)

# Send Message
message_textbox = tk.Entry(bottom_frame, font=FONT,
                           bg=MEDIUM_GREY, fg=WHITE, width=37)
message_textbox.pack(side=tk.LEFT, padx=5)

message_button = tk.Button(bottom_frame, text="Send", font=BUTTON_FONT,
                           bg=OCEAN_BLUE, fg=WHITE, command=send_message)
message_button.pack(side=tk.LEFT, padx=5)


# main function

def main():
    root.mainloop()


if __name__ == '__main__':
    main()
