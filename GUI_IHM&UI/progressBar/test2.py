import tkinter
import tkinter.ttk

def run():
    progressbarOne.start()

def stop():
    progressbarOne.stop()


root = tkinter.Tk()
root.geometry('150x120')

progressbarOne = tkinter.ttk.Progressbar(root, length=200, mode='determinate', orient=tkinter.HORIZONTAL)
progressbarOne.pack(padx=5, pady=10)

progressbarOne['maximum'] = 100
progressbarOne['value'] = 0

buttonRun = tkinter.Button(root, text='Run', width=6, command=run)
buttonRun.pack(padx=10, pady=5, side=tkinter.LEFT)

buttonStop = tkinter.Button(root, text='Stop', width=6, command=stop)
buttonStop.pack(padx=10, pady=5, side=tkinter.RIGHT)

root.mainloop()
