import tkinter as tk
from tkinter import filedialog


window = tk.Tk()
window.title("tirer les fichiers")
window.geometry("400x300")

drop_area = tk.Label(window,text="ici", bg="white",width=40,height=20)

def drag_enter(event):
    drop_area.config(bg="lightblue")

def drag_leave(event):
    drop_area.config(bg="white")

def drag_drop(event):
    drop_area.config(bg="white")
    # file_path = filedialog.askopenfilename()
    file_path = filedialog.askdirectory()


    # file_path = event.data
    print(file_path)
    # show_file_path(file_path)

drop_area.bind("<Enter>",drag_enter)
drop_area.bind("<Leave>",drag_leave)
drop_area.bind("<ButtonRelease-1>",drag_drop)

drop_area.pack()






window.mainloop()