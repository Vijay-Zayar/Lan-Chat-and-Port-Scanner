import tkinter
from tkinter import messagebox
import socket
def scan():
    ipadd=shmpentryhost.get()
    portno1=shmpentryport1.get()
    portno1=int(portno1)
    portno2=shmpentryport2.get()
    portno2=int(portno2)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result=''
    for portno in range(portno1,portno2+1):

        if sock.connect_ex((ipadd,portno)):
            result+=f'Port {portno} is closed in host {ipadd}\n'

        else :
            result+=f'Port {portno} is opened in host {ipadd}\n'
    messagebox.showinfo('Scan Result',result)
    sock.close()
shmp=tkinter.Tk()
shmplabelhost=tkinter.Label(shmp,text='Enter IP Address')
shmpentryhost=tkinter.Entry(shmp,bd=5)
shmplabelport1=tkinter.Label(shmp, text='Start Port Number(1 to 65535)')
shmpentryport1 = tkinter.Entry(shmp, bd=5)
shmplabelport2=tkinter.Label(shmp, text='End Port Number(1 to 65535)')
shmpentryport2 = tkinter.Entry(shmp, bd=5)
shmpbtn=tkinter.Button(shmp,text='Scan',command=scan)
shmplabelhost.pack()
shmpentryhost.pack()
shmplabelport1.pack()
shmpentryport1.pack()
shmplabelport2.pack()
shmpentryport2.pack()
shmpbtn.pack()
tkinter.mainloop()