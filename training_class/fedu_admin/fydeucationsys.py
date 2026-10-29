from tkinter import *
from tkinter.messagebox import *
import service,adminmain

class RegisterLoginWin():
    def __init__(self):
        self.loginwin = Tk()
        self.loginwin.title('邦邦培训-后台管理系统')
        self.loginwin.geometry('360x240+600+200')
        self.loginwin.configure(bg='#E5FFDD')
        self.loginwin.resizable(False, False)
        # 布局用户名和密码
        Label(self.loginwin, text='用户名:', bg='#E5FFDD').place(x=55, y=110, width=60, height=25)
        self.entry_user = Entry(self.loginwin)
        self.entry_user.place(x=135, y=110, width=150, height=25)
        # 密码
        Label(self.loginwin, text='密 码:', bg='#E5FFDD').place(x=55, y=145, width=60, height=25)
        self.entry_pwd = Entry(self.loginwin, show='*')
        self.entry_pwd.place(x=135, y=145, width=150, height=25)
        # 三个按钮
        Button(self.loginwin, text='注册', bg='green', fg='white', command=self.register).place(x=100, y=180,width=60,height=40)
        Button(self.loginwin, text='登录', bg='green', fg='white', command=self.login).place(x=170, y=180,width=60,height=40)
        Button(self.loginwin, text='退出', bg='green', fg='white', command=self.loginwin.destroy).place(x=240,y=180,width=60,height=40)

        self.loginwin.mainloop()

    #登录函数
    def login(self):
        admin_name=self.entry_user.get()
        admin_pwd=self.entry_pwd.get()
        if admin_name=='' or admin_pwd=='':
            showwarning('警告','登录名或密码不允许为空')
            return False
        # 登录是查询
        sql='select id from t_admin where admin_name=%s and admin_pwd=%s'
        #result的结果是什么数据类型((4,),)
        result=service.query(sql,admin_name,admin_pwd)
        if len(result)>0:
            # 模块名.类名() ,调用AdminWin()中的__init__方法去执行
            # 传值，模块与模块之间进行传值
            adminmain.admin_id=result[0][0] # 元组取值 ((4,),)
            adminmain.admin_pwd=self.entry_pwd.get()
            adminmain.objmain=self #self指代的是谁？RegisterLoginWin类的对象
            self.loginwin.withdraw()
            adminmain.AdminWin() #登录成功，实现跳转，跳转到主窗体

        else:
            showerror('错误','登录名或密码不正确')

    def register(self):
        admin_name=self.entry_user.get() # 获取单行文本框中的值
        admin_pwd=self.entry_pwd.get()
        if admin_name=='' or admin_pwd=='':
            showwarning('警告','用户名或密码不能为空')
            return False
        # 加一个用户名重复的判断
        sql = 'select * from t_admin where admin_name=%s'
        queryresult = service.query(sql, admin_name)  #
        if len(queryresult) > 0:
            showwarning('警告', '用户已注册，请更换用户名')
        else:

            # 注册操作 ，属于增，删，改，查中的增
            sql = 'insert into t_admin(admin_name,admin_pwd) values (%s,%s)'
            # service是自定义的模块exec是自定义函数中的函数
            result = service.exec(sql, (admin_name, admin_pwd))
            if result > 0:
                showinfo('提示', '注册成功')
            else:
                showerror('错误', '注册失败，请联系管员')
        # 清空文本框中的值
        self.entry_user.delete(0, END)
        self.entry_pwd.delete(0, END)
RegisterLoginWin()