import tkinter as tk 
import os
import tkinter.messagebox 

window = tk.Tk()

window.title("Mon fenetre")

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('750x550')

l0 = tk.Label(window, text='Saisir le repertoire origine (avec/ à la fin):', bg='green', font=('Arial', 12), width=60, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 放置lable的方法有：1）l.pack(); 2)l.place();
l1 = tk.Label(window, text='Saisir le repertoire sortie (avec/ à la fin):', bg='green', font=('Arial', 12), width=60, height=2)



e0 = tk.Entry(window, show=None, font=('Arial', 11),width=68)
e1 = tk.Entry(window, show=None, font=('Arial', 11),width=68)



var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
a = tk.Label(window, textvariable=var, bg='gray', fg='white', font=('Arial', 10), width=100, height=20)





on_hit = False
def valider():
    global on_hit
    if on_hit == False:
        on_hit = True
        # var.set('you hit me')
    else:
        on_hit = False

    if os.path.isdir(e0.get()) and os.path.isdir(e1.get()): 
        var.set("le repertoire origine : "+e0.get()+"\nle repertoire sortie: "+e1.get())
    else :
        tk.messagebox.showerror(title='Erro', message="c'est pas une bonne repertoire !!")
b = tk.Button(window, text='Valider', font=('Arial', 12), width=10, height=1, command=valider)

    




# l1.pack(side ="left")
l0.pack(pady=10)    
e0.pack(ipady=3)    
l1.pack(pady=10)  
e1.pack(ipady=3)    
b.pack(pady=5)
a.pack(ipady=3,ipadx=3,pady=25)








window.mainloop()