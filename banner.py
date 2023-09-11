import socket
import tkinter
from tkinter import messagebox
def retBanner():
    s=socket.socket()
    ip=hostentry.get()
    port=portentry.get()
    port=int(port)
    try:
        s.connect((ip,port))
        try:
            banner=s.recv(1024)
            messagebox.showinfo('Banner Result',banner)
        except:
            messagebox.showerror('Banner Result','Cannot retrieve baanner!')
    except:
        messagebox.showerror('Banner Error','Sorry! Cannot make connection!!!')

banner=tkinter.Tk()
hostlabel=tkinter.Label(banner,text='Enter IP Address')
hostlabel.pack()
hostentry=tkinter.Entry(banner,bd=5)
hostentry.pack()
portlabel=tkinter.Label(banner,text='Enter Port No')
portlabel.pack()
portentry=tkinter.Entry(banner,bd=2)
portentry.pack()
bannerbtn=tkinter.Button(banner,text='Look Banner',command=retBanner)
bannerbtn.pack()
tkinter.mainloop()
