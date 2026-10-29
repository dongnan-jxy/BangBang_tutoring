from tkinter import *
from tkinter.messagebox import *
from unittest import result

import service,teacher,student


# 初始化窗口
class LoginEducation():
    def __init__(self):
        self.loginwin = Tk()  # 创建窗口
        self.loginwin.title('邦邦培训注册/登录')
        self.loginwin.geometry('360x240+600+200')  # 设置窗口位置，距y轴600，x轴200
        self.loginwin.resizable(width=False, height=False)  # 不可改变窗口大小
        self.loginwin.config(bg='#E5FFDD')  # 设置颜色
        # 设置背景图片,添加进去
        self.img = PhotoImage(file='images/bj.png')
        Label(self.loginwin, image=self.img).place(x=0, y=0, width=360, height=98)
        # 添加组件                             设置text的背景颜色
        Label(self.loginwin, text='用户角色', bg='#E5FFDD').place(x=60, y=110, width=80, height=20)  # place定位，设置位置
        self.rolev = IntVar()
        self.rolev.set(1)
        self.r1 = Radiobutton(self.loginwin, text='学员', bg='#E5FFDD', variable=self.rolev, value=1)
        self.r2 = Radiobutton(self.loginwin, text='老师', bg='#E5FFDD', variable=self.rolev, value=0)
        self.r1.place(x=140, y=110, width=60, height=20)
        self.r2.place(x=210, y=110, width=80, height=20)
        #   添加用户名和登录密码
        Label(self.loginwin, text='用户名：', bg='#E5FFDD').place(x=60, y=140, width=80, height=20)
        self.entry_user = Entry(self.loginwin)
        self.entry_user.place(x=140, y=140, width=140, height=20)
        Label(self.loginwin, text='密码：', bg='#E5FFDD').place(x=60, y=170, width=80, height=20)
        self.entry_pwd = Entry(self.loginwin, show='*')
        self.entry_pwd.place(x=140, y=170, width=140, height=20)

        # 三个按钮
        Button(self.loginwin, text="注册", bg='green', fg='white', command=self.register).place(x=100, y=200, width=60,
                                                                                                height=25)
        Button(self.loginwin, text="登录", bg='green', fg='white', command=self.login).place(x=170, y=200, width=60,
                                                                                             height=25)
        Button(self.loginwin, text="退出", bg='green', fg='white',command=self.loginwin.destroy).place(x=240, y=200,
                                                                                                          width=60,
                                                                                                          height=25)

        self.loginwin.mainloop()

    # 设计注册功能
    def register(self):
        username = self.entry_user.get()  # 从单行文本框读取数据
        pwd = self.entry_pwd.get()
        if username == '' or pwd == '':
            showwarning("警告", '请输入用户名或密码')
            return False
        elif self.rolev.get() == 0:
            sql = 'insert into t_teacher(username,pwd)values(%s,%s)'
            result = service.exec(sql, (username, pwd))
            if result > 0:
                showwarning('提示', '注册成功')
                # 清空数据
                self.entry_pwd.delete(0, 'end')
                self.entry_user.delete(0, 'end')
        else:
            #注册学员
            sql='insert into t_student(login_name,login_pwd) values(%s,%s)'
            result = service.exec(sql, (username, pwd))
            if result > 0:
                showinfo('提示','学员注册成功')
                self.entry_pwd.delete(0, 'end')
                self.entry_user.delete(0, 'end')
            else:
                showwarning('警告','注册学员失败')

    # 设计登录功能
    def login(self):
        username = self.entry_user.get()
        pwd = self.entry_pwd.get()
        if username == '' or pwd == '':
            showwarning('警告','用户名账号密码不能为空')
            return False
        else:
            if self.rolev.get() == 0:
                sql='select id from t_teacher where username = %s and pwd = %s'
                result = service.query(sql, username, pwd)
                if len(result) > 0:
                    #打开教员窗体
                    #窗口隐藏
                    self.loginwin.withdraw()
                    #将当前窗口传递给teacher的objmain
                    teacher.objmain=self
                    teacher.teacher_id = result[0][0]
                    teacher.teacher_pwd = self.entry_pwd.get()

                    teacher.TeacherWin()
                else:
                    showwarning('警告','用户名或密码不存在')
            else:
                #学员登录
                sql='select id from t_student where login_name = %s and login_pwd = %s'
                result = service.query(sql, username, pwd)
                if len(result) > 0:
                    #登陆成功之后切换界面
                    self.loginwin.withdraw()
                    student.objmain=self
                    student.student_pwd=pwd
                    student.student_id = result[0][0]
                    student.StudentWin()#创建对象

                else:
                    showwarning('警告','用户名或密码不正确')
LoginEducation()
