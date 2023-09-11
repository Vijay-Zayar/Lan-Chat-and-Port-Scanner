import tkinter
import os
def shspscan(ipadd,portno):
    print(ipadd)
    print(portno)

def shsp():
    os.system('python shsp.py')
def shmp():
    os.system('python shmp.py')
def banner():
    os.system('python banner.py')
contaner=tkinter.Tk()
label=tkinter.Label(contaner,text='Welcome to Port Scanner.This program will help for your security')
psbtn1=tkinter.Button(contaner,text='Single host && Single port',command=shsp)
psbtn2=tkinter.Button(contaner,text='Single host && Multiple ports',command=shmp)
psbtn3=tkinter.Button(contaner,text='Banner from open port of a Specific host',command=banner)
label.pack()
psbtn1.pack()
psbtn2.pack()
psbtn3.pack()
tkinter.mainloop()