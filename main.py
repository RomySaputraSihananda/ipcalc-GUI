import tkinter as tk;
from tkinter import ttk;
from tkinter.messagebox import showinfo;
from utils import getIP;

canvas = tk.Tk();

canvas.configure(bg='#3e3e3e');
canvas.geometry('300x200');
canvas.resizable(False,False);
canvas.title('IP CALCULATOR');

# Frame
frame = ttk.Frame(canvas);
frame.pack(padx=10, pady=10, fill='x', expand=True);

# components

# label
ip_label = ttk.Label(frame, text='Massukan IP ex : 192.168.0.1/24');
ip_label.pack(padx=50, pady=10, fill='x', expand=True);

# input
ip = tk.StringVar();
ip_entry = ttk.Entry(frame, textvariable=ip);
ip_entry.pack(padx=20, pady=10, fill='x', expand=True);

# button
def calculate():
    showinfo(title='HASIL.....', message=getIP(ip.get()));

submit = ttk.Button(frame, text='Hitung', command=calculate);
submit.pack(padx=100, fill='x', expand=True);

canvas.mainloop();