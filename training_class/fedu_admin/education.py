#coding:utf-8
from tkinter import *
from tkinter.messagebox import *
import service,area  # 导入了省份，区域模块
adminmainobj=None # 存储主窗体的对象

class EductionWin():
    def __init__(self,insert,update,delete,query):
        self.eduwin=Toplevel()
        self.eduwin.title('邦邦培训-后台管理系统')
        self.eduwin.geometry('350x250+600+200')
        self.eduwin.configure(bg='#E5FFDD')
        self.eduwin.resizable(False, False)


        self.eduwin.mainloop()