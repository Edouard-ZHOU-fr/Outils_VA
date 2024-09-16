from tkinter import *
window = Tk()
window.title("亲情导出")
window.geometry('400x300')
import tkinter.filedialog
 
e1 = Label(window, text="路径：")#这是标签
e1.grid(row=1,column=0)
g = Entry(window,width=40)#这是输入框
g.grid(row=1, column=1,columnspan=1)
 
def se():#这是获取路径函数
    g.delete(0, "end")
    path=filedialog.askopenfilename()
    path=path.replace("/","\\\\")#通过replace函数替换绝对文件地址中的/来使文件可被程序读取 #注意：\\转义后为\，所以\\\\转义后为\\
    g.insert('insert',path)
 
 
b1 = Button(window, text="查询", command=se)#这是按键
b1.grid(row=1, column=3)
 
window.mainloop()
