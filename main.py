# -*- coding:utf-8 -*-
# 开始解析txt行数
count = len(open('classmates.txt','r',encoding="utf-8").readlines())
count -= 1
print(count)
#作为元组导入
with open("classmates.txt", "r", encoding='utf-8') as f:  #打开文本
    data = f.read()   #读取文本
    print(data)
a=data.split("\n")
print(a)
import random
# 导入tkinter
import tkinter as tk
from tkinter import messagebox
root_window =tk.Tk()
# 设置窗口title
root_window.title('''看看谁是范进''')
# 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
root_window.geometry('350x250')
# 更改左上角窗口的的icon图标
root_window.iconphoto(False, tk.PhotoImage(file='./images/me.ico'))
# 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
root_window["background"] = "#C9C9C9"
# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text=tk.Label(root_window,text="已载入%s个名字"%count,bg="white",fg="black",font=('Times', 20, 'bold'))
# 将文本内容放置在主窗口内
text.pack()
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button=tk.Button(root_window,text="关闭",command=root_window.quit)
#添加按钮以及生成随机数
def A():
    b = (random.randint(1,count))
    print(b)
    global a
    zhu = a[b]
    print(zhu)
    messagebox.showinfo(title='范进中举',message='%s:噫！我中了！'%zhu)
button2=tk.Button(root_window,text="开始",command=A,height=30,width=100)
# 将按钮放置在主窗口内
button.pack(side="bottom",padx=10,pady=10)
button2.pack(side='top',padx=10,pady=10,)
#进入主循环，显示主窗口
root_window.mainloop()