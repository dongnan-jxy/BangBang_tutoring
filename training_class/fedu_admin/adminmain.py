from tkinter import *
from tkinter.messagebox import *
import service,area
admin_id = 0    #整数
admin_pwd = ''  #字符串值
objmain=None

class AdminWin():
    def __init__(self):
        self.adminwin = Toplevel()
        self.adminwin.title('邦邦培训-后台管理系统')
        self.adminwin.geometry('795x490+600+200')
        self.adminwin.configure(bg='#E5FFDD')
        self.adminwin.resizable(False, False)
        # 添加菜单
        self.menu_main = Menu(self.adminwin)  # 主
        self.menu1 = Menu(self.menu_main, tearoff=False)  # 子
        self.menu2 = Menu(self.menu_main, tearoff=False)
        self.menu3 = Menu(self.menu_main, tearoff=False)
        self.menu4 = Menu(self.menu_main, tearoff=False)
        self.menu5 = Menu(self.menu_main, tearoff=False)
        self.menu6 = Menu(self.menu_main, tearoff=False)
        self.menu7 = Menu(self.menu_main, tearoff=False)
        self.menu8 = Menu(self.menu_main, tearoff=False)
        self.menu9 = Menu(self.menu_main, tearoff=False)
        self.menu10 = Menu(self.menu_main, tearoff=False)
        # 为主菜单添加菜单项
        self.menu_main.add_cascade(label='管理员管理', menu=self.menu1)
        self.menu_main.add_cascade(label='省份管理', menu=self.menu2)
        self.menu_main.add_cascade(label='学历管理', menu=self.menu3)
        self.menu_main.add_cascade(label='教师身份管理', menu=self.menu4)
        self.menu_main.add_cascade(label='区域管理', menu=self.menu5)
        self.menu_main.add_cascade(label='教授方法管理', menu=self.menu6)
        self.menu_main.add_cascade(label='教师管理', menu=self.menu7)
        self.menu_main.add_cascade(label='学生管理', menu=self.menu8)
        self.menu_main.add_cascade(label='培训管理', menu=self.menu9)
        self.menu_main.add_cascade(label='评价管理', menu=self.menu10)
        # 还可以继续添 年级管理和课程管理
        # 为每一个菜单项，添加子菜单
        self.menu1.add_command(label='修改密码', command=self.modifypwd)
        # 省份管理
        self.menu2.add_command(label='添加省份',command=self.addprovince)
        self.menu2.add_command(label='修改省份',command=self.modifyprovince)
        self.menu2.add_command(label='删除省份',command=self.deleteprovince)
        self.menu2.add_command(label='查询省份',command=self.queryprovince)
        # 学历管理
        self.menu3.add_command(label='添加学历')
        self.menu3.add_command(label='修改学历')
        self.menu3.add_command(label='删除学历')
        self.menu3.add_command(label='查询学历')
        # 教员身份管理
        self.menu4.add_command(label='添加教员身份')
        self.menu4.add_command(label='修改教员身份')
        self.menu4.add_command(label='删除教员身份')
        self.menu4.add_command(label='查询教员身份')
        # 区域管理
        self.menu5.add_command(label='添加区域')
        self.menu5.add_command(label='修改区域')
        self.menu5.add_command(label='删除区域')
        self.menu5.add_command(label='查询区域')
        # 教授方法管理
        self.menu6.add_command(label='添加教授方法')
        self.menu6.add_command(label='修改教授方法')
        self.menu6.add_command(label='删除教授方法')
        self.menu6.add_command(label='查询教授方法')
        # 教员管理
        self.menu7.add_command(label='查询教师')  # 增，删，改，同学自己扩展
        # 学员管理
        self.menu8.add_command(label='查询学生')
        # 家教管理
        self.menu9.add_command(label='查询需求')
        # 评价管理
        self.menu10.add_command(label='评价管理')

        # 将主菜单添加到窗体上
        self.adminwin.config(menu=self.menu_main)


        self.adminwin.bind('<Destroy>', self.on_tolevel_close)
        self.adminwin.mainloop()

    def queryprovince(self):
        area.adminmainobj = self  # self是谁?
        self.adminwin.withdraw()
        # insert传True，说明 添加按钮有效，其它三个按钮禁用
        area.AreaWin(False, False, False, True)

    def modifyprovince(self):
        area.adminmainobj = self  # self是谁?
        self.adminwin.withdraw()
        # insert传True，说明 添加按钮有效，其它三个按钮禁用
        area.AreaWin(False, True, False, False)

    def deleteprovince(self):
        area.adminmainobj = self  # self是谁?
        self.adminwin.withdraw()
        # insert传True，说明 添加按钮有效，其它三个按钮禁用
        area.AreaWin(False, False, True, False)

    # 打开添加窗体
    def addprovince(self):
        #模块名.类名()创建对象 ，每次打开子窗体时，主窗体都要隐藏
        # 主窗体要与省份窗体之间有沟通，
        # 省份窗体打开之前，主窗体隐藏，在省份窗体关闭后，主窗体再显示
        area.adminmainobj=self  # self是谁?
        self.adminwin.withdraw()
        # insert传True，说明 添加按钮有效，其它三个按钮禁用
        area.AreaWin(True,False,False,False)
    #修改管理员密码
    def modifypwd(self):
        #修改密码时，让主窗体隐藏，打开修改密码窗体
        self.adminwin.withdraw()
        self.pwdwin=Toplevel()
        self.pwdwin.title('邦邦培训-后台管理系统-修改管理员密码')
        self.pwdwin.geometry('388x290+600+200')
        self.pwdwin.configure(bg='#E5FFDD')
        self.pwdwin.resizable(False, False)
        img=PhotoImage(file='./images/changepwd.png')
        Label(self.pwdwin,image=img).place(x=10,y=10,width=378,height=280)
        # 文本框
        self.oldpwd=Entry(self.pwdwin,show='*')
        self.oldpwd.insert(0,admin_pwd)
        self.oldpwd.config(state='readonly')
        self.oldpwd.place(x=150,y=95,width=200,height=25)
        # 新密码和确认密码
        self.newpwd=Entry(self.pwdwin,show='*')
        self.newpwd.place(x=150,y=130,width=200,height=25)

        self.compwd = Entry(self.pwdwin, show='*')
        self.compwd.place(x=150, y=165, width=200, height=25)
        # 确定和取消
        Button(self.pwdwin,text='确定',bg='green',fg='white',command=self.updatepwd).place(x=180,y=220,width=60,height=40)
        Button(self.pwdwin, text='取消', bg='green', fg='white',command=self.close).place(x=250, y=220, width=60, height=40)

        self.pwdwin.mainloop()

    #修改密码
    def updatepwd(self):
        if self.newpwd.get()=='' or self.compwd.get()=='':
            showerror('警告','新密码或确认密码不能为空')
            return False
        if self.newpwd.get()!=self.compwd.get():
            showerror('警告','确认密码与新密码不一致')
        else:
            sql='update t_admin set admin_pwd=%s where id=%s'
            result=service.exec(sql,(self.newpwd.get(),admin_id))
            if result>0:
                showinfo('提示','修改管理员密码成功')
                # 将当前窗体关闭
                # 将主窗体打开
                self.close()
            else:
                showerror('错误','修改管理员密码失败')

    def close(self): # 关闭当前窗体，将主窗体进行显示
        self.pwdwin.destroy()
        #把主窗体显示
        self.adminwin.deiconify()

    def on_tolevel_close(self,event): # 因为是绑定的事件，所以要加event，可以不用，但是不能没有
        # 在登录成功之后把定义登录窗体的类的对象传给了objmain
        #objmain.loginwin.deiconify() # 登录窗体再显示
        objmain.loginwin.destroy() # 登录窗体跟关闭

# AdminWin()