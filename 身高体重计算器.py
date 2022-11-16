import tkinter.ttk
import tkinter.messagebox
import tkinter
from tkinter import filedialog
import os
import time as t

def starta():
    root0 = tkinter.Tk()
    root0.geometry('900x300+300+160')
    root0.resizable(False, False)
    root0.title("身高/体重计算器")

    bH1 = tkinter.Label(root0, text='请输入身高:')
    bH1.place(x=170, y=80, width=150, height=25)
    bH1 = tkinter.Label(root0, text='单位:厘米(cm)')
    bH1.place(x=520, y=80, width=120, height=25)

    bZ1 = tkinter.Label(root0, text='请输入体重:')
    bZ1.place(x=170, y=140, width=150, height=25)
    bZ1 = tkinter.Label(root0, text='单位:公斤(kg)')
    bZ1.place(x=520, y=140, width=120, height=25)

    entryH = tkinter.Entry(root0)
    entryH.place(x=350, y=80, width=150, height=25)
    entryZ = tkinter.Entry(root0)
    entryZ.place(x=350, y=140, width=150, height=25)

    def buttonClick():
        bR1 = tkinter.Label(root0, text='计算完成!你的身高是:' + entryH.get() + '厘米!')
        bR1.place(x=170, y=180, width=250, height=25)
    def buttonClick1():
        bF1 = tkinter.Label(root0, text='计算完成!你的体重是:' + entryZ.get() + '公斤!')
        bF1.place(x=170, y=200, width=250, height=25)

    buttonStart = tkinter.Button(root0, text='开始', command=buttonClick)
    buttonStart.place(x=680, y=80, width=75, height=25)
    buttonStart1 = tkinter.Button(root0, text='开始', command=buttonClick1)
    buttonStart1.place(x=680, y=140, width=75, height=25)

    root0.bind('<Return>', lambda event=None: buttonStart.invoke())
    root0.bind('<Return>', lambda event=None: buttonStart1.invoke())

    tkinter.mainloop()

if __name__ == '__main__':
    starta()
