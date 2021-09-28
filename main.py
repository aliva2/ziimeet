import tkinter as tk
from tkinter import messagebox

def btn_click():
  login = loginInput.get()
  password = passField.get()

  info_str = f'Dati: {str(login)}, {str(password)}'
  messagebox.showinfo(title='Nosaukums', message=info_str)

  #kļūdu logs
  #messagebox.showerror(title = '', message = 'Error')

win = tk.Tk() # pilveertiigs logs
# platumu x garumu + noKreisaas + noAugshas
win.geometry(f"400x300+10+20")
win['bg'] = '#7C51A0'
win.title('Programmas nosaukums')
win.wm_attributes('-alpha', 0.9)


#objekts canvas grafikasveidoshanai
canvas = tk.Canvas(win, height=200, width = 300 )
canvas.pack()

#ietvaraa klasee Frame vieglaak straadaat ar objektiem
frame = tk.Frame(win, bg = 'white')
# veido klases Frame objektu 0.15=15%, 1=100%
frame.place(relx=0.15, rely=0.15, relwidth = 0.7, relheight=0.5)

title2 = tk.Label(frame, text='Darbibas logs', bg = 'green')
title2.pack()
btn = tk.Button(frame, text='Poga', bg='yellow', command=btn_click)
btn.pack()

loginInput = tk.Entry(frame, bg='white')
loginInput.pack()

passField = tk.Entry(frame, bg='white', show='*')
passField.pack()


win.mainloop()