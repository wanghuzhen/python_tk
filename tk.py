'''
Author: Wang Huzhen
Version: 1.0
FilePath: \undefinedc:\Users\whz\Desktop\tk\tk_gui\tk.py
Email: 2327253081@qq.com
Date: 2021-04-15 15:47:15
'''

from tkinter import *
import tkinter.filedialog
from tkinter.font import Font
from PIL import ImageTk, Image

root_window = Tk()
root_window.title('家居场景分割')
root_window.geometry('1400x600')
filename = ''

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)


def scrollbar(frm):
    canvas=Canvas(frm)
    frame=Frame(canvas)
    myscrollbar=Scrollbar(frm,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",myfunction)


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


# 目标检测
def detectron():
    global filename
    if filename != '':
        img_png = Image.open(filename).resize((300, 300))
        img = ImageTk.PhotoImage(img_png)
        lb_scene_res_pic.config(image=img)
        lb_scene_res_pic.image = img

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
scrollbar(f2_2)

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
scrollbar(f3_1)
scrollbar(f3_2)
f3_1.place(x=10, y=70)
f3_1.propagate(0)
f3_2.place(x=270, y=70)
f3_2.propagate(0)
f3.place(x=870, y=50)
f3.propagate(0)
root_window.mainloop()
