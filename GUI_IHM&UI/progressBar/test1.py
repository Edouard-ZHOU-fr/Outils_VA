import time
import tkinter
import tkinter.ttk
def show():
    # 设置进度条的目前值
    progressbarOne['value'] = 0
    # 设置进度条的最大值
    progressbarOne['maximum'] = maxbyte
    # 调用loading方法
    loading()

def loading():
    # 改变变量属性
    global byte
    # 每次运行500B
    byte += 500
    # 设置指针
    progressbarOne['value'] = byte
    if byte < maxbyte:
        # 经过100ms后再次调用loading方法
        progressbarOne.after(100, loading)


root = tkinter.Tk()
root.geometry('150x120')

# 设置下载初值
byte = 0
# 设置下载最大值
maxbyte = 10000

progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)

button = tkinter.Button(root, text='Running', command=show)
button.pack(pady=5)

root.mainloop()

