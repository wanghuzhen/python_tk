'''
Author: Wang Huzhen
Version: 1.0
FilePath: \tk\tk_gui\scrollbar.py
Email: 2327253081@qq.com
Date: 2021-04-15 19:33:20
'''
from tkinter import *
import os
import cv2
from PIL import ImageTk,Image

def label_pic(img,f,w,h,fn):
    print(h,w)
    f_tmp = Frame(f,height=h,width=270,bg='green')
    lb = Label(f_tmp,image = img,height=h, width=w)
    lb.image = img
    lb.pack()
    f_tmp.grid()
    f_tmp.propagate(0)
    la = Label(f,text=fn)
    la.grid()


def data(f):
    # for i in range(50):
    #    Label(frame,text=i).grid(row=i,column=0)
    #    Label(frame,text="my text"+str(i)).grid(row=i,column=1)
    #    Label(frame,text="..........").grid(row=i,column=2)
    path = r'C:\Users\whz\Desktop\tk\0000005/'
    print(path)
    for filename in os.listdir(path):
        if '-' in filename:
            tmp = cv2.imread(path+'/'+filename)
            # print(int(tmp.shape[0]/3), int(tmp.shape[1]/3))
            img_png = Image.open(path+filename).resize((int(tmp.shape[1]/3), int(tmp.shape[0]/3)))
            img = ImageTk.PhotoImage(img_png)
            label_pic(img,f,int(tmp.shape[1]/3),int(tmp.shape[0]/3),filename)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root=Tk()

root.geometry('290x470')

myframe=Frame(root,relief=GROOVE,width=290,height=470,bd=1,bg='red')
myframe.place(x=0,y=0)
myframe.propagate(0)
canvas=Canvas(myframe,bg='red')
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left",fill = 'both',expand = 'yes')
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
data(frame)
root.mainloop()
