import tkinter
from tkinter import messagebox
import socket
def scan():
    ipadd=shspentryhost.get()
    portno=shspentryport.get()
    portno=int(portno)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((ipadd,portno)):
        messagebox.showinfo('Scan Results',f'Port {portno} is closed in host {ipadd}')

    else :
        messagebox.showinfo('Scan Results',f'Port {portno} is opened in host {ipadd}')
    sock.close()
shsp=tkinter.Tk()
shsplabelhost=tkinter.Label(shsp,text='Enter IP Address')
shspentryhost=tkinter.Entry(shsp,bd=5)
shsplabelport=tkinter.Label(shsp, text='Enter Port Number(1 to 65535)')
shspentryport = tkinter.Entry(shsp, bd=5)
shspbtn=tkinter.Button(shsp,text='Scan',command=scan)
shsplabelhost.pack()
shspentryhost.pack()
shsplabelport.pack()
shspentryport.pack()
shspbtn.pack()
tkinter.mainloop()