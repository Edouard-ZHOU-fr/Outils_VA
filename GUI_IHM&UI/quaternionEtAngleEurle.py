import tkinter as tk 
import os
import tkinter.messagebox 
import tkinter.ttk

import numpy as np
import math

def quaternion_to_euler_angle_vectorized1(w, x, y, z):
    ysqr = y * y

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + ysqr)
    X = np.degrees(np.arctan2(t0, t1))

    t2 = +2.0 * (w * y - z * x)
    t2 = np.where(t2>+1.0,+1.0,t2)
    #t2 = +1.0 if t2 > +1.0 else t2

    t2 = np.where(t2<-1.0, -1.0, t2)
    #t2 = -1.0 if t2 < -1.0 else t2
    Y = np.degrees(np.arcsin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (ysqr + z * z)
    Z = np.degrees(np.arctan2(t3, t4))
    return X, Y, Z 


def get_quaternion_from_euler(roll, pitch, yaw):
  """
  Convert an Euler angle to a quaternion.
   
  Input
    :param roll: The roll (rotation around x-axis) angle in radians.
    :param pitch: The pitch (rotation around y-axis) angle in radians.
    :param yaw: The yaw (rotation around z-axis) angle in radians.
 
  Output
    :return qx, qy, qz, qw: The orientation in quaternion [x,y,z,w] format
  """
  qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
  qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
  qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
  qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
 
  return [qx, qy, qz, qw]

def degree2Radians(degree):
    return ((degree*math.pi)/180 )

def radians2Degree(radians):
    return ((radians*180)/math.pi )



def valider():
    x = float(e0.get())
    y = float(e1.get())
    z = float(e2.get())
    w = float(e3.get())

    X,Y,Z = quaternion_to_euler_angle_vectorized1(w,x,y,z)
    drapeau = var1.get()
    print(drapeau)
    if drapeau :
        z_radians = degree2Radians(Z)
        s_z_radians = str(z_radians)
        var.set('Radians: ' + s_z_radians)
        window.update()

    else : 
        s_z = str(Z)
        var.set('Degree: ' + s_z)

        window.update()



window = tk.Tk()
window.title("Quaternion2Eurle")
window.geometry('400x450')
window.resizable(False, False)

l0 = tk.Label(window, text='Quaternion X: ', bg='green', font=('Arial', 11), width=15, height=2)
l1 = tk.Label(window, text='Quaternion Y: ', bg='green', font=('Arial', 11), width=15, height=2)
l2 = tk.Label(window, text='Quaternion Z: ', bg='green', font=('Arial', 11), width=15, height=2)
l3 = tk.Label(window, text='Quaternion W: ', bg='green', font=('Arial', 11), width=15, height=2)
l4 = tk.Label(window, text="l'angle sortie est en degree par defaut ", bg='yellow', font=('Arial', 8), width=40, height=2)
l5 = tk.Label(window, text="Angle Eurle yaw: ", bg='green', font=('Arial', 10), width=20, height=2)


e0 = tk.Entry(window, show=None, font=('Arial', 12),width=22)
e1 = tk.Entry(window, show=None, font=('Arial', 12),width=22)
e2 = tk.Entry(window, show=None, font=('Arial', 12),width=22)
e3 = tk.Entry(window, show=None, font=('Arial', 12),width=22)

b = tk.Button(window, text='Valider', font=('Arial', 13), width=10, height=1, command=valider)




var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Radians',font=('Arial', 11),variable=var1, onvalue=1, offvalue=0) 

var = tk.StringVar()    
a = tk.Label(window, textvariable=var, bg='gray', fg='white', font=('Arial', 11), width=26, height=2)

# x = 0
# y = 0
# z = 0.656677770043545
# w = 0.7541712712180417 


# x = 0
# y = 0
# z = -0.12287527827022567
# w = 0.9924221208689449 




# 

# x_radians = degree2Radians(X)
# y_radians = degree2Radians(Y)
# z_radians = degree2Radians(Z)

# print("\n"+"X(Roll):"+str(X)+"°\nY(Pitch):"+str(Y)+"°\nZ(Yaw):"+str(Z)+"°\n")
# print("\n"+"X(Roll):"+str(x_radians)+"[radians]\nY(Pitch):"+str(y_radians)+
#         "[radians]\nZ(Yaw):"+str(z_radians)+"[radians]\n")


l0.grid(column=0, row=0,pady=8)   # grid dynamically divides the space in a grid
l1.grid(column=0, row=1,pady=8)
l2.grid(column=0, row=2,pady=8)
l3.grid(column=0, row=3,pady=8)
l4.grid(column=1, row=5,pady=0)
l5.grid(column=0, row=6,pady=0)




e0.grid(column=1, row=0,ipady=3,padx=5) 
e1.grid(column=1, row=1,ipady=3,padx=5)    
e2.grid(column=1, row=2,ipady=3,padx=5)    
e3.grid(column=1, row=3,ipady=3,padx=5)   

b.grid(column=0, row=4,pady=5,padx=5)
c1.grid(column=1, row=4,pady=5,padx=5)

a.grid(column=1, row=6,pady=5,padx=5,ipady=1)





window.mainloop()






