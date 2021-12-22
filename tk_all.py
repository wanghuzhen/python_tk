# '''
# Author: Wang Huzhen
# Version: 1.0
# FilePath: \undefinedc:\Users\whz\Desktop\tk\tk_gui\tk.py
# Email: 2327253081@qq.com
# Date: 2021-04-15 15:47:15
# '''
from tkinter import *
import tkinter.filedialog
from tkinter.font import Font
from PIL import ImageTk, Image
import os
import cv2

root_window = Tk()
root_window.title('家居场景分割')
root_window.geometry('1400x600')
filename = ''


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas_2.configure(scrollregion=canvas.bbox("all"))
    canvas_3.configure(scrollregion=canvas.bbox("all"))


def xz():
    global filename
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        lb.config(text="您选择的文件是："+filename)
        img_png = Image.open(filename).resize((300, 300))
        img = ImageTk.PhotoImage(img_png)
        lb_scene.config(image=img)
        lb_scene.image = img
    else:
        lb.config(text="您没有选择任何文件")


def label_pic(img,f,w,h,fn):
    print(h,w)
    f_tmp = Frame(f,height=h,width=170)
    lb = Label(f_tmp,image = img,height=h, width=w)
    lb.image = img
    lb.pack()
    f_tmp.grid()
    f_tmp.propagate(0)
    la = Label(f,text=fn)
    la.grid()


# data
def data(s,f):
    path = s+'/'
    # print(path)
    for filename in os.listdir(path):
        if '-' in filename:
            tmp = cv2.imread(path+'/'+filename)
            # print(int(tmp.shape[0]/3), int(tmp.shape[1]/3))
            img_png = Image.open(path+filename).resize((int(tmp.shape[1]/3), int(tmp.shape[0]/3)))
            img = ImageTk.PhotoImage(img_png)
            label_pic(img,f,int(tmp.shape[1]/3),int(tmp.shape[0]/3),filename)


# 目标检测
def detectron():
    global filename
    # index = int(filename.split('/')[5].split('.')[0])
    # print(filename.split('/')[6].split('.')[0])
    data(filename.split('/')[6].split('.')[0],frame)
    data(filename.split('/')[6].split('.')[0],frame_2)
    data(filename.split('/')[6].split('.')[0],frame_3)
    # if filename != '':
    #     img_png = Image.open(filename).resize((300, 300))
    #     img = ImageTk.PhotoImage(img_png)
    #     lb_scene_res_pic.config(image=img)
    #     lb_scene_res_pic.image = img

btn = Button(root_window, text="家居图片选择菜单", command=xz)
btn.place(x=0, y=0, bordermode=INSIDE)
lb = Label(root_window, text='', font=Font(size=16))
lb.place(x=120, y=0, bordermode=INSIDE)
f1 = Frame(root_window, height=550, width=340,
           relief=tkinter.RIDGE, borderwidth=5)
f1_1 = Frame(f1, height=300, width=300)
f2 = Frame(root_window, height=550, width=530,
           relief=tkinter.RIDGE, borderwidth=5)
f2_1 = Frame(f2, height=300, width=300)
f2_2 = Frame(f2, height=470, width=190,relief=GROOVE,bd=1)
f3 = Frame(root_window, height=550, width=530,
           relief=tkinter.RIDGE, borderwidth=5)
f3_1 = Frame(f3, height=470, width=245,relief=GROOVE,bd=1)
f3_2 = Frame(f3, height=470, width=245,relief=GROOVE,bd=1)

# frame1
lb_scene_des = Label(f1, text='家居场景图', font=Font(size=16))
lb_scene_des.place(x=120, y=0)
lb_scene = Label(f1_1, height=300, width=300)
lb_scene.place(x=0, y=0)
btn_2 = Button(f1, text="目标检测", command=detectron, fg='red')
btn_2.place(x=140, y=360, bordermode=INSIDE)
btn_3 = Button(f1, text="模型检索", command=detectron, fg='red')
btn_3.place(x=140, y=410, bordermode=INSIDE)
f1_1.place(x=15, y=40)
f1_1.propagate(0)
f1.place(y=50)
f1.propagate(0)
# frame2
lb_scene_des = Label(f2, text='目标检测结果显示', font=Font(size=16))
lb_scene_des.pack(side=TOP)
lb_scene_res = Label(f2, text='家居图片预测框图', font=Font(size=14))
lb_scene_res.place(x=60, y=40)
lb_scene_sub = Label(f2, text='切割家居子图', font=Font(size=14))
lb_scene_sub.place(x=340, y=40)
# 显示预测图
lb_scene_res_pic = Label(f2_1, height=300, width=300,bg='red')
lb_scene_res_pic.place(x=0, y=0)
# 此处滑动窗口
canvas=Canvas(f2_2)
frame=Frame(canvas)
myscrollbar=Scrollbar(f2_2,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left",fill = 'both',expand = 'yes')
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)


f2_1.place(x=10, y=70)
f2_1.propagate(0)
f2_2.place(x=320, y=70)
f2_2.propagate(0)
f2.place(x=340, y=50)
f2.propagate(0)

# frame3
lb_scene_3D_res = Label(f3, text='三维家居模型检索结果显示', font=Font(size=16))
lb_scene_3D_res.pack(side=TOP)
muti_view_1 = Label(f3, text='最相似角度多视图', font=Font(size=14))
muti_view_1.place(x=60, y=40)
muti_view_2 = Label(f3, text='多视图对应家居模型', font=Font(size=14))
muti_view_2.place(x=300, y=40)
# scrollbar(f3_1)
canvas_2=Canvas(f3_1)
frame_2=Frame(canvas_2)
myscrollbar=Scrollbar(f3_1,orient="vertical",command=canvas_2.yview)
canvas_2.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
canvas_2.pack(side="left",fill = 'both',expand = 'yes')
canvas_2.create_window((0,0),window=frame_2,anchor='nw')
frame_2.bind("<Configure>",myfunction)
# scrollbar(f3_2)
canvas_3=Canvas(f3_2)
frame_3=Frame(canvas_3)
myscrollbar=Scrollbar(f3_2,orient="vertical",command=canvas_3.yview)
canvas_3.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
canvas_3.pack(side="left",fill = 'both',expand = 'yes')
canvas_3.create_window((0,0),window=frame_3,anchor='nw')
frame_3.bind("<Configure>",myfunction)

f3_1.place(x=10, y=70)
f3_1.propagate(0)
f3_2.place(x=270, y=70)
f3_2.propagate(0)
f3.place(x=870, y=50)
f3.propagate(0)
root_window.mainloop()
