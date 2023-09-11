import os
import tkinter
import socket
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 15)
BUTTON_FONT = ("Helvetica", 14)
SMALL_FONT = ("Helvetica", 12)
# def portscanner():
#     os.system('python portscanner.py')


def get_local_ip():
    # Get the local IP address of the machine
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def servergc():
    os.system('python server.py')


def clientgc():
    os.system('python client.py')


def main():

    gc = tkinter.Tk()
    gc.title('Messenger for the Classroom')
    gc.geometry("500x500")
    gc.config(bg=MEDIUM_GREY)

    style = Style()
    style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'),
                    foreground='red')

    gclabel = Label(gc, text='Please choose mode of group chat')
    gcserver = Button(gc, text='Make Server', command=servergc)
    # server_message_box = Entry(gc)
    # server_message_box.config(state=tkinter.DISABLED)

    gcclient = Button(gc, text='Make Client', command=clientgc)
    quit_btn = Button(gc, text='Quit',
                      style='W.TButton', command=gc.quit)

    gclabel.pack()
    gcserver.pack()
    # server_message_box.pack()
    gcclient.pack()
    quit_btn.pack()

    tkinter.mainloop()


if __name__ == '__main__':
    main()
