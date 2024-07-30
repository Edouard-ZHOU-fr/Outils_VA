import tkinter as tk
from tkinter import ttk
 
root = tk.Tk()
root.geometry('300x200+5+5')
root.title('a selectable message')
 
btn1 = ttk.Button(root,text="mybtn1",takefocus=0)
btn2 = ttk.Button(root,text="mybtn2",takefocus=0)
 
selectableMsg = tk.Text(root,width=35,height=4,relief='flat',bg='gray94',
wrap='word',font=('consolas','9'))
 
myinfo = 'How to use a tkinter text widget to creat a selectable message widght, this is a example code'
 
selectableMsg.insert(1.0,myinfo)
selectableMsg.configure(state='disabled')
 
btn1.pack(pady=5)
selectableMsg.pack(pady=5)
btn2.pack(pady=5)
 
root.mainloop()

