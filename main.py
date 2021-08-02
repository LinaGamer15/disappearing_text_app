import string
from tkinter import *
import tkinter.ttk as ttk
import copy

ws = Tk()
ws.title('Disappearing Text Writing App')
ws.geometry('810x500')
ws['bg'] = 'gray22'

t_f = False

time_after = 3000

count_times = 0


def result(text):
    print(text)
    table = str.maketrans(dict.fromkeys(string.punctuation))
    new_text = text.translate(table)
    print(new_text)
    result_words = str(len(new_text.split(' ')))
    print(result_words)
    ttk.Label(ws, text=f'Result: {result_words} words', style='BW.TLabel').grid(row=4, column=1, pady=20)


def disappear():
    global t_f, len_entry1, entry, ws, count_times
    len_entry = len(entry.get(1.0, END))
    if count_times == 0:
        result(entry.get(1.0, END))
        entry.grid_forget()
    if not t_f:
        if len_entry == len_entry1:
            t_f = True
            ws.after(time_after, disappear)
            count_times -= 1
    elif len_entry == len_entry1 and t_f:
        result(entry.get(1.0, END))
        entry.grid_forget()
        len_entry1 = len(entry.get(1.0, END))
        t_f = False
        disappear()
    elif t_f:
        len_entry1 = copy.copy(len_entry)
        t_f = False
        disappear()


def start():
    global count_times
    if clicked.get() != 'Select time':
        error.grid_forget()
        button.grid_forget()
        entry.grid(row=3, column=1, pady=20)
        count_times = 60000 * int(clicked.get()) // time_after
        disappear()
    else:
        error.grid(row=1, column=1, pady=10)


style_bold = ttk.Style()
style_bold.configure('Bold.TLabel', background='gray22', foreground='white', font=('Sans', '30', 'bold'))
style_normal = ttk.Style()
style_normal.configure('BW.TLabel', background='gray22', foreground='white', font=('Sans', '12', 'normal'))
style_button = ttk.Style()
style_button.configure('Bold.TButton', font=('Sans', '12', 'normal'))

title = ttk.Label(ws, text='Disappearing Text Writing App', style='Bold.TLabel').grid(row=0, column=1)
error = ttk.Label(ws, text='To get started, you need to choose a time', style='BW.TLabel')
time = ttk.Label(ws, text='Time in minutes:', style='BW.TLabel').grid(row=2, column=0, pady=20, padx=10)
options = ['Select time', '1', '5', '10', '15']
clicked = StringVar()
clicked.set(options[0])
select_time = ttk.OptionMenu(ws, clicked, *options).grid(row=2, column=2, pady=20)

button = ttk.Button(ws, text='Start', width=15, style='Bold.TButton', command=start)
button.grid(row=3, column=1, pady=20)

entry = Text(ws, height=15, width=60, font='Sans 12')

len_entry1 = len(entry.get(1.0, END))

ws.mainloop()
