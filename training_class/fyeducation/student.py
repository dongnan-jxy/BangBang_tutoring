from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview

objmain = None  # 代表主窗口登录窗口
student_id = 1
student_pwd = ""
from training_class.fyeducation import service


class StudentWin():
    def __init__(self):
        self.win = Toplevel()
        self.win.title('邦邦培训班-学生端')
        self.win.geometry('1500x900+0+0')
        self.win.configure(bg='#E5FFDD')
        self.win.resizable(width=False, height=False)
        self.img = PhotoImage(file='images/teacherbj.png')
        Label(self.win, image=self.img).place(x=0, y=0, width=1700, height=980)
        # 两个标签七个按钮
        Label(self.win, text='培训管理', bg='#E5FFDD').place(x=400, y=110, width=80, height=25)
        Button(self.win, text='我的订单', bg='green', fg='white',command=self.showorder).place(x=400, y=135,
                                                                        width=80,
                                                                        height=40)
        Button(self.win, text='预约老师', bg='green', fg='white', command=self.appointment_teacher).place(
            x=490, y=135, width=80, height=40)
        Button(self.win, text='评价老师', bg='green', fg='white',command=self.evaluation).place(x=400, y=185,
                                                                        width=80,
                                                                        height=40)

        Label(self.win, text='账户管理', bg='#E5FFDD', ).place(x=400, y=250, width=80, height=25)
        Button(self.win, text='基本信息', bg='green', fg='white',command=self.showstuinfo).place(x=400, y=285,
                                                                        width=80,
                                                                        height=40)
        Button(self.win, text='更改密码', bg='green', fg='white',command=self.modifypwd).place(x=490, y=285,
                                                                        width=80,
                                                                        height=40)
        Button(self.win, text='完善信息', bg='green', fg='white',command=self.wanshanupdate).place(x=400,
                                                                        y=335,
                                                                        width=80,
                                                                        height=40)
        Button(self.win, text='修改信息', bg='green', fg='white',command=self.modifystudent).place(x=490,
                                                                        y=335,
                                                                        width=80,
                                                                        height=40)

        # 发布需求
        Label(self.win, text='发布需求', bg='#E5FFDD').place(x=700, y=110, width=80, height=25)
        # 年级
        Label(self.win, text='就读年级：', bg='#E5FFDD').place(x=600, y=145, width=100, height=25)
        # 读取所有年级
        self.lst_gradename = query_grade()
        self.gradev = StringVar()
        self.gradev.set(self.lst_gradename[0])
        self.grade = Combobox(self.win, textvariable=self.gradev, values=self.lst_gradename)
        self.grade.place(x=710, y=145, width=200, height=25)

        # 学生性别
        Label(self.win, text='学生性别：', bg='#E5FFDD').place(x=605, y=180, width=100, height=25)
        self.genderv = IntVar()
        self.genderv.set(1)  # 1表示男生，0表示女生
        self.rdgender1 = Radiobutton(self.win, text='男', variable=self.genderv, value=1, bg='#E5FFDD')
        self.rdgender2 = Radiobutton(self.win, text='女', variable=self.genderv, value=0, bg='#E5FFDD')
        self.rdgender1.place(x=710, y=180, width=60, height=25)
        self.rdgender2.place(x=780, y=180, width=60, height=25)
        # 辅导科目
        Label(self.win, text='辅导科目：', bg='#E5FFDD').place(x=600, y=215, width=100, height=25)
        # 根据所选择的年级名称，获取年级id
        self.gradeid = get_gradeid_by_name(self.gradev.get())
        # 根据年级id查询对应的课程
        self.lst_course = get_course_by_grade(self.gradeid)
        self.coursev = StringVar()
        self.coursev.set(self.lst_course[0])
        self.course = Combobox(self.win, textvariable=self.coursev, values=self.lst_course)
        self.course.place(x=710, y=215, width=200, height=25)
        # 授课时间
        Label(self.win, text='授课时间：', bg='#E5FFDD').place(x=600, y=250, width=100, height=25)
        t_time1 = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        t_time2 = ['上午', '下午', '晚上']
        self.t_timev1 = StringVar()
        self.t_timev1.set(t_time1[0])
        self.t_timev2 = StringVar()
        self.t_timev2.set(t_time2[0])
        self.t_time1 = Combobox(self.win, textvariable=self.t_timev1, values=t_time1)
        self.t_time2 = Combobox(self.win, textvariable=self.t_timev2, values=t_time2)
        self.t_time1.place(x=710, y=250, width=95, height=25)
        self.t_time2.place(x=815, y=250, width=95, height=25)
        # 授课区域
        Label(self.win, text='授课区域：', bg='#E5FFDD').place(x=600, y=285, width=100, height=25)
        # 查询所有的区域
        self.lst_district = query_district()
        self.districtv = StringVar()
        self.districtv.set(self.lst_district[0])
        self.district = Combobox(self.win, textvariable=self.districtv, values=self.lst_district)
        self.district.place(x=710, y=285, width=200, height=25)
        # 授课地址
        Label(self.win, text='授课地址：', bg='#E5FFDD').place(x=600, y=320, width=100, height=25)
        self.address = Entry(self.win)
        self.address.place(x=710, y=320, width=200, height=25)
        # 联系人
        Label(self.win, text='联系人：', bg='#E5FFDD').place(x=600, y=355, width=100, height=25)
        self.contacts = Entry(self.win)
        self.contacts.place(x=710, y=355, width=200, height=25)
        # 联系电话
        Label(self.win, text='联系电话：', bg='#E5FFDD').place(x=600, y=390, width=100, height=25)
        self.phone = Entry(self.win)
        self.phone.place(x=710, y=390, width=200, height=25)
        # 微信
        Label(self.win, text='微    信：', bg='#E5FFDD').place(x=600, y=425, width=100, height=25)
        self.wchat = Entry(self.win)
        self.wchat.place(x=710, y=425, width=200, height=25)
        # 学习状况
        Label(self.win, text='学习状况：', bg='#E5FFDD').place(x=600, y=460, width=100, height=25)
        self.study = Text(self.win)
        self.study.place(x=710, y=460, width=200, height=60)
        # 薪酬标准
        Label(self.win, text='薪酬标准：', bg='#E5FFDD').place(x=600, y=530, width=100, height=25)
        self.salary = Spinbox(self.win, from_=60, to=120, increment=10)
        self.salary.place(x=710, y=530, width=160, height=25)
        Label(self.win, text='元/时', bg='#E5FFDD').place(x=880, y=530, width=40, height=25)
        # 教员性别
        Label(self.win, text='老师性别：', bg='#E5FFDD').place(x=600, y=565, width=100, height=25)
        self.teacher_genderv = IntVar()
        self.teacher_genderv.set(1)  # 1表示男
        self.teacher_rdgender1 = Radiobutton(self.win, bg='#E5FFDD', variable=self.teacher_genderv, text='男', value=1)
        self.teacher_rdgender2 = Radiobutton(self.win, bg='#E5FFDD', variable=self.teacher_genderv, text='女', value=0)
        self.teacher_rdgender3 = Radiobutton(self.win, bg='#E5FFDD', variable=self.teacher_genderv, text='不限',
                                             value=-1)
        self.teacher_rdgender1.place(x=710, y=565, width=40, height=25)
        self.teacher_rdgender2.place(x=770, y=565, width=40, height=25)
        self.teacher_rdgender3.place(x=820, y=565, width=50, height=25)
        # 教员的身份
        Label(self.win, text='老师身份：', bg='#E5FFDD').place(x=600, y=600, width=100, height=25)
        self.lst_identity = query_identity()
        self.identityv = StringVar()
        self.identityv.set(self.lst_identity[0])
        self.identity = Combobox(self.win, textvariable=self.identityv, values=self.lst_identity)
        self.identity.place(x=710, y=600, width=200, height=25)
        # 授课方式
        Label(self.win, text='授课方式：', bg='#E5FFDD').place(x=600, y=635, width=100, height=25)
        self.lst_teachmethod = query_teachmethod()
        self.teachmethodv = StringVar()
        self.teachmethodv.set(self.lst_teachmethod[0])
        self.teachmethod = Combobox(self.win, textvariable=self.teachmethodv, values=self.lst_teachmethod)
        self.teachmethod.place(x=710, y=635, width=200, height=25)
        # 对教员的要求
        Label(self.win, text='对老师要求：', bg='#E5FFDD').place(x=600, y=670, width=100, height=25)
        self.teach_require = Text(self.win)
        self.teach_require.place(x=710, y=670, width=200, height=60)
        # 两个按钮，一个发布 需求，一个 取消
        Button(self.win, text='发布需求', bg='green', fg='white', command=self.publishreq).place(x=650, y=750,
                                                                                                 width=100,
                                                                                                 height=40)
        Button(self.win, text='取消', bg='green', fg='white',command=self.clear).place(x=760, y=750, width=70,
                                                                                        height=40)
        self.win.bind('<Destroy>', self.on_toplevel_close)



        self.win.mainloop()

    #
    def on_toplevel_close(self,event):
        objmain.loginwin.deiconify()
        objmain.entry_user.delete(0, END)
        objmain.entry_pwd.delete(0, END)

    #修改密码
    def modifypwd(self):
        modifypwdwin = Toplevel()
        modifypwdwin.title('邦邦培训-学生端-更改密码')
        modifypwdwin.geometry('300x250+600+200')
        modifypwdwin.configure(bg='#E5FFDD')
        modifypwdwin.resizable(False, False)
        Label(modifypwdwin, text='更改登录密码', bg='#E5FFDD', fg='green').place(x=100, y=20, width=120,height=25)
        Label(modifypwdwin, text='原密码：', bg='#E5FFDD').place(x=10, y=60, width=70, height=25)
        self.stupwd = Entry(modifypwdwin, show='*')
        self.stupwd.place(x=90, y=60, width=180, height=25)
        self.stupwd.insert(0, student_pwd)
        self.stupwd.configure(state='readonly')#只读

        print(student_pwd)

        # 新密码
        Label(modifypwdwin, text='新密码：', bg='#E5FFDD').place(x=10, y=95, width=70, height=25)
        self.stunewpwd = Entry(modifypwdwin, show='*')
        self.stunewpwd.place(x=90, y=95, width=180, height=25)
        # 确认密码
        Label(modifypwdwin, text='确认密码：', bg='#E5FFDD').place(x=10, y=130, width=80, height=25)
        self.stucompwd = Entry(modifypwdwin, show='*')
        self.stucompwd.place(x=90, y=130, width=180, height=25)
        # 两个Button
        Button(modifypwdwin, text='确定', bg='green', fg='white', command=self.updatepwd).place(x=100, y=170,width=60,height=40)
        Button(modifypwdwin, text='取消', bg='green', fg='white', command=modifypwdwin.destroy).place(x=170,y=170,width=60,height=40)
        modifypwdwin.mainloop()

    #修改登录密码，操作数据库
    def updatepwd(self):
        newpwd=self.stunewpwd.get() # 获取新密码
        compwd=self.stucompwd.get() # 获取确认密码
        if newpwd=='' or compwd=='':
            showerror('警告','新密码和确认密码均不允许为空')
            return False
        else:
            if newpwd==compwd:
                sql='update t_student set login_pwd=%s where id=%s'
                result= service.exec(sql, (newpwd, student_id))
                if result>0:
                    showinfo('提示','修改密码成功，下次登录有效')
                    self.stunewpwd.delete(0,END)
                    self.stucompwd.delete(0,END)
                else:
                    showerror('错误','修改密码失败，请联系管理员')
            else:
                showerror('错误','密码和确认密码不一致')

    #修改个人信息
    def modifystudent(self):
        # 加载当前登录的学生的个人信息
        sql = 'select student_name,gender,address,wchat from t_student where id=%s'
        result = service.query(sql, student_id)
        modifywin = Toplevel()
        modifywin.geometry('300x250+600+200')
        modifywin.configure(bg='#E5FFDD')
        modifywin.resizable(False, False)
        Label(modifywin, text='修改个人信息', bg='#E5FFDD', fg='green').place(x=100, y=20, width=120,height=25)
        Label(modifywin, text='姓名：', bg='#E5FFDD').place(x=10, y=55, width=60, height=25)
        self.modi_studentname = Entry(modifywin)
        self.modi_studentname.place(x=80, y=55, width=200, height=25)
        self.modi_studentname.insert(0, result[0][0])
        # 性别
        Label(modifywin, text='性别：', bg='#E5FFDD').place(x=10, y=90, width=60, height=25)
        self.modi_genderv = IntVar()
        self.modi_genderv.set(1 if result[0][1] == '男' else 0)
        self.modi_gender1 = Radiobutton(modifywin, text='男', variable=self.modi_genderv, value=1, bg='#E5FFDD')
        self.modi_gender1.place(x=80, y=90, width=60, height=25)
        self.modi_gender2 = Radiobutton(modifywin, text='女', variable=self.modi_genderv, value=0, bg='#E5FFDD')
        self.modi_gender2.place(x=150, y=90, width=60, height=25)
        # 地址
        Label(modifywin, text='地址：', bg='#E5FFDD').place(x=10, y=125, width=60, height=25)
        self.modi_student_address = Entry(modifywin)
        self.modi_student_address.place(x=80, y=125, width=200, height=25)
        self.modi_student_address.insert(0, result[0][2])
        # 微信
        Label(modifywin, text='微信：', bg='#E5FFDD').place(x=10, y=160, width=60, height=25)
        self.modi_student_wchat = Entry(modifywin)
        self.modi_student_wchat.place(x=80, y=160, width=200, height=25)
        self.modi_student_wchat.insert(0, result[0][3])
        # 两个 按钮，确定和取消
        Button(modifywin, text='确认修改', bg='green', fg='white', command=self.updatestudent).place(x=110,
                                                                                                              y=200,
                                                                                                              width=80,
                                                                                                              height=40)
        Button(modifywin, text='取消', bg='green', fg='white', command=modifywin.destroy).place(x=200, y=200,
                                                                                                         width=60,
                                                                                                         height=40)

        modifywin.mainloop()

    #修改个人信息
    def updatestudent(self):
        sql='update t_student set student_name=%s,gender=%s,address=%s,wchat=%s where id =%s'
        gender='男' if self.modi_genderv.get()==1 else '女'
        result= service.exec(sql, (self.modi_studentname.get(), gender, self.modi_student_address.get(), self.modi_student_wchat.get(), student_id))
        if result>0:
            showinfo('提示','修改个人信息成功')
        else:
            showerror('错误','修改个人信息失败，请联系管理员')

    #完善个人信息
    def wanshanupdate(self):
        # 完善个人信息
        updateinfowin=Toplevel()
        updateinfowin.title('邦邦培训-学生端-完善个人信息')
        updateinfowin.geometry('300x250+600+200')
        updateinfowin.configure(bg='#E5FFDD')
        updateinfowin.resizable(False, False)
        Label(updateinfowin,text='完善个人信息',bg='#E5FFDD',fg='green').place(x=100,y=20,width=120,height=25)
        Label(updateinfowin,text='姓名：',bg='#E5FFDD').place(x=10,y=55,width=60,height=25)
        self.student_name=Entry(updateinfowin)
        self.student_name.place(x=80,y=55,width=200,height=25)
        # 性别
        Label(updateinfowin, text='性别：', bg='#E5FFDD').place(x=10, y=90, width=60, height=25)
        self.studentgenderv=IntVar()
        self.studentgenderv.set(1)# 1表示男
        self.studentgender1=Radiobutton(updateinfowin,text='男',variable=self.studentgenderv,value=1,bg='#E5FFDD')
        self.studentgender2 = Radiobutton(updateinfowin, text='女', variable=self.studentgenderv, value=0, bg='#E5FFDD')
        self.studentgender1.place(x=80,y=90,width=60,height=25)
        self.studentgender2.place(x=150, y=90, width=60, height=25)
        # 地址
        Label(updateinfowin, text='地址：', bg='#E5FFDD').place(x=10, y=125, width=60, height=25)
        self.student_address=Entry(updateinfowin)
        self.student_address.place(x=80,y=125,width=200,height=25)
        # 微信
        Label(updateinfowin, text='微信：', bg='#E5FFDD').place(x=10, y=160, width=60, height=25)
        self.student_wchat = Entry(updateinfowin)
        self.student_wchat.place(x=80, y=160, width=200, height=25)
        # 两个按钮一个确定，一个取消
        Button(updateinfowin,text='确定',bg='green',fg='white',command=self.wanshanstudent).place(x=110,y=200,width=60,height=40)
        Button(updateinfowin, text='取消', bg='green', fg='white',command=updateinfowin.destroy).place(x=180, y=200, width=60, height=40)
        updateinfowin.mainloop()

    #完善个人信息
    def wanshanstudent(self):
        sql = 'update t_student set student_name=%s,gender=%s,address=%s,wchat=%s where id =%s'
        gender = '男' if self.studentgenderv.get() == 1 else '女'
        result = service.exec(sql,
                              (self.student_name.get(), gender, self.student_address.get(), self.student_wchat.get(),
                               student_id))
        if result > 0:
            showinfo('提示', '完善个人信息成功')
            self.student_name.delete(0, END)
            self.student_address.delete(0, END)
            self.student_wchat.delete(0, END)
            self.studentgenderv.set(1)  # 默认选中男
        else:
            showerror('错误', '完善个人信息失败，请联系管理员')

    #显示学生信息
    def showstuinfo(self):
        sql = 'select student_name from t_student where id=%s'
        result = service.query(sql, student_id)
        if result[0][0] == None:
            showerror('警告', '请先完善个人信息')
        else:
            #显示个人信息
            showstudentinfo=Toplevel()
            showstudentinfo.title('邦邦培训-学生端-查看个人信息')
            showstudentinfo.geometry('300x250+600+200')
            showstudentinfo.configure(bg='#E5FFDD')
            showstudentinfo.resizable(False, False)
            sql='select student_name,gender,address,wchat from t_student where id=%s'
            result= service.query(sql, student_id)
            Label(showstudentinfo,text='显示个人信息',bg='#E5FFDD',fg='green').place(x=100,y=20,width=120,height=25)
            Label(showstudentinfo, text='姓名：', bg='#E5FFDD' ).place(x=10, y=55, width=60,height=25)
            Label(showstudentinfo, text=result[0][0], bg='#E5FFDD').place(x=80, y=55, width=60,height=25)
            # 性别
            Label(showstudentinfo, text='性别：', bg='#E5FFDD',).place(x=10, y=90, width=60, height=25)
            Label(showstudentinfo, text=result[0][1], bg='#E5FFDD').place(x=80, y=90, width=60, height=25)
            # 地址
            Label(showstudentinfo, text='地址：', bg='#E5FFDD',).place(x=10, y=125, width=60, height=25)
            Label(showstudentinfo, text=result[0][2], bg='#E5FFDD').place(x=80, y=125, width=120, height=25)
            # 微信
            Label(showstudentinfo, text='微信：', bg='#E5FFDD',).place(x=10, y=160, width=60, height=25)
            Label(showstudentinfo, text=result[0][3], bg='#E5FFDD').place(x=80, y=160, width=120, height=25)
            showstudentinfo.mainloop()

    #打开评价老师窗口
    def evaluation(self):
        self.evlwin = Toplevel()
        self.evlwin.title('邦邦培训-学生端-评价教师')
        self.evlwin.geometry('400x300+600+200')
        self.evlwin.configure(bg='#E5FFDD')
        self.evlwin.resizable(False, False)
        # 页面布局
        Label(self.evlwin, text='选择评价教师:', bg='#E5FFDD').place(x=10, y=10, width=120, height=25)
        #组合框
        lst_teacher_name = query_teachername()
        self.teacher_namev = StringVar()
        self.teacher_namev.set(lst_teacher_name[0])
        self.teacher_name = Combobox(self.evlwin, textvariable=self.teacher_namev, values=lst_teacher_name)
        self.teacher_name.place(x=140,y=10,width=100,height=25)
        # 评价内容
        Label(self.evlwin, text='评价内容:', bg='#E5FFDD').place(x=10, y=45, width=80, height=25)
        self.evlcontent = Text(self.evlwin)
        self.evlcontent.place(x=15, y=80, width=370, height=100)
        # 三个按钮
        Button(self.evlwin, text='提交评价', bg='green', fg='white', command=self.submitevl).place(x=100,
                                                                                                            y=200,
                                                                                                            width=80,
                                                                                                            height=40)
        Button(self.evlwin, text='取消', bg='green', fg='white', command=self.evlwin.destroy).place(x=190,
                                                                                                             y=200,
                                                                                                             width=80,
                                                                                                             height=40)
        Button(self.evlwin, text='查看评价', bg='green', fg='white', command=self.showevl).place(x=280, y=200,
                                                                                                          width=80,
                                                                                                          height=40)
        self.evlwin.mainloop()

    #查看评价
    def showevl(self):
        self.evlwin.withdraw()#隐藏评价窗口
        self.showevlwin = Toplevel()
        self.showevlwin.title('邦邦培训-学生端-查看评价')
        self.showevlwin.geometry('400x350+600+200')
        self.showevlwin.configure(bg='#E5FFDD')
        self.showevlwin.resizable(False, False)
        lst = ['id', 'student_name', 'teacher_name', 'content']
        lst_name = ['序号', '学生姓名', '老师姓名', '评价内容']
        self.treev = tv(self.showevlwin,lst,lst_name)
        self.treev.place(x=10,y=10,width=380,height=150)
        self.treev.bind('<Double-Button-1>',self.get_data)
        #在treeview中显示数据
        sql = 'select e.id,s.student_name,t.teacher_name,e.content from t_student as s inner join t_evaluation as e on s.id=e.student_id inner join t_teacher as t on t.id=e.teacher_id where e.student_id=%s order by id '
        result = service.query(sql, student_id)
        tv_data(self.treev, result)
        # 修改评价的多行文本框
        Label(self.showevlwin,text='修改评价:',bg='#E5FFDD').place(x=10,y=170,width=80,height=25)
        self.evaluation=Text(self.showevlwin)
        self.evaluation.place(x=100,y=170,width=290,height=100)
        # 三个按钮
        Button(self.showevlwin, text='修改评价', bg='green', fg='white', command=self.modifyevl).place(x=110,
                                                                                                                y=290,
                                                                                                                width=80,
                                                                                                                height=40)

        Button(self.showevlwin, text='删除评价', bg='green', fg='white', command=self.deleteevl).place(x=200,
                                                                                                                y=290,
                                                                                                                width=80,
                                                                                                                height=40)

        Button(self.showevlwin, text='返回', bg='green', fg='white', command=self.callback).place(x=290, y=290,
                                                                                                           width=80,
                                                                                                           height=40)

        self.evlwin.mainloop()

    #修改评价
    def modifyevl(self):
        if self.treev.focus()=='':
            showerror('警告','请先选中一条要修改的评价')
        else:
            sql = 'update t_evaluation set content=%s where id=%s'
            result = service.exec(sql, (self.evaluation.get('0.0', END), self.evl_id))
            if result > 0:
                showinfo('提示', '修改评价成功')
                # 更新treeview数据
                # 删除评价成功之后，要重新向treeview添加数据
                sql = 'select e.id,s.student_name,t.teacher_name,e.content from t_student as s inner join t_evaluation as e on s.id=e.student_id inner join t_teacher as t on t.id=e.teacher_id where e.student_id=%s order by id '
                result = service.query(sql, student_id)
                tv_data(self.treev, result)
                # 将多行文本框的内容清空
                self.evaluation.delete('0.0', END)
            else:
                showerror('错误', '修改评价失败，请联系管理员')

    #删除评价1
    def deleteevl(self):
        if self.treev.focus() == '':
            showerror('警告', '请先选择要删除的评价')
        else:
            # 获取id，根据id删除评价
            iid = self.treev.focus()
            # 根据iid获取选中行数据
            item = self.treev.item(iid)  # item是字典类型
            values = item.get('values')  # 字典取值,values是列表类型
            evl_id = values[0]
            sql = 'delete from t_evaluation where id=%s'
            result = service.exec(sql, evl_id)
            if result > 0:
                showinfo('提示', '删除评价成功')
                # 删除评价成功之后，要重新向treeview添加数据
                sql = 'select e.id,s.student_name,t.teacher_name,e.content from t_student as s inner join t_evaluation as e on s.id=e.student_id inner join t_teacher as t on t.id=e.teacher_id where e.student_id=%s order by id '
                result = service.query(sql, student_id)
                tv_data(self.treev, result)
            else:
                showerror('错误', '删除评价出错，请联系管理员')

    #1
    def callback(self):
        self.showevlwin.destroy()  # 关闭显示评价窗体
        self.evlwin.deiconify()  # 显示评价讲师窗体

    # 提交评价1
    def submitevl(self):
        # 获取讲师的id
        teacher_id = query_teacher_id_by_name(self.teacher_name.get())
        content = self.evlcontent.get('0.0', END).strip()  # 使用strip把默认空格去掉
        print(len(content))
        if content != '':
            sql = 'insert into t_evaluation (student_id,teacher_id,content)values (%s,%s,%s)'
            result = service.exec(sql, (student_id, teacher_id, content))
            if result > 0:
                showinfo('提示', '提交评价成功')
                self.evlcontent.delete('0.0', END)
            else:
                showerror('错误', '提交评价出错，请联系管理员')
        else:
            showerror('警告', '评价内容不允许为空')

    #查看订单1
    def showorder(self):
        orderwin = Toplevel()
        orderwin.title('邦邦培训-学生端-我的订单')
        orderwin.geometry('1000x500+30+30')
        orderwin.configure(bg='#E5FFDD')
        orderwin.resizable(False, False)
        lst = ['student_id', 'student_name', 'education', 'school', 'major', 'teach_time', 'teacherwchat', 'contacts',
               'phone', 'course_name', 'gradename']
        lst_name = ['序号', '学生姓名', '讲师的最高学历', '毕业院校', '讲师专业', '授课时间', '讲师微信', '学生联系人',
                    '联系电话', '课程名称', '年级']

        treev=tv(orderwin,lst,lst_name)
        treev.place(x=50,y=50,width=900,height=350)
        # 显示数据
        sql = 'select DISTINCT * from showorderinfo'
        result = service.query2(sql)
        tv_data(treev, result)
        # 添加一个返回按钮
        Button(orderwin, text='返回', bg='green', fg='white', command=orderwin.destroy).place(x=450, y=420,width=80,height=40)
        orderwin.mainloop()

    # 发布需求的方法1
    def publishreq(self):
        grade_id = get_id_by_name('select id from t_grade where gradename=%s', self.gradev.get())
        course_id = get_id_by_name2('select id from t_course where course_name=%s and grade_id=%s', self.coursev.get(),
                                    grade_id)
        district_id = get_id_by_name('select id from t_district where district=%s', self.districtv.get())
        identity_id = get_id_by_name('select id from t_identity where identity=%s', self.identityv.get())
        teach_method_id = get_id_by_name('select id from t_teachmethod where teachmethod=%s', self.teachmethodv.get())
        student_gender = '男' if self.genderv.get() == 1 else '女'
        teacher_gender = '男' if self.teacher_genderv.get() == 1 else (
            '女' if self.teacher_genderv.get() == 0 else '不限')
        sql = 'insert into t_fastorderteacher(student_id,course_id,study_time,district_id,address,contacts,phone,wchat,study,teacher_gender,salary,identity_id,teach_method_id,teach_require,grade_id,stu_gender)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        result = service.exec(sql, (student_id, course_id, self.t_timev1.get() + ' ' + self.t_timev2.get(),
                                    district_id, self.address.get(), self.contacts.get(),
                                    self.phone.get(), self.wchat.get(), self.study.get('0.0', END),
                                    teacher_gender, eval(self.salary.get()), identity_id,
                                    teach_method_id, self.teach_require.get('0.0', END), grade_id, student_gender))
        if result > 0:
            showinfo('提示', '需求发布成功')
            self.clear()
        else:
            showerror('错误', '需求发布失败')

        # 负责清空 发布需求框中的值

    def clear(self):
        self.gradev.set(self.lst_gradename[0])
        self.genderv.set(1)  # 学生性别默认为1
        self.coursev.set(self.lst_course[0])
        self.t_timev1.set('星期一')
        self.t_timev2.set('上午')
        self.address.delete(0, END)
        self.contacts.delete(0, END)
        self.phone.delete(0, END)
        self.wchat.delete(0, END)
        self.study.delete('0.0', END)
        # Spinbox
        self.salary.delete(0, END)
        self.salary.insert(0, '60')
        self.teacher_genderv.set(1)  # 1表示男，0表示女-1表示不限
        # 教员身份
        self.identityv.set(self.lst_identity[0])
        self.teachmethodv.set(self.lst_teachmethod[0])
        self.teach_require.delete('0.0', END)

    # 预约讲师1
    def appointment_teacher(self):
        # 显示所有的教师
        # 显示所有的教师
        self.appointmentwin = Toplevel()
        self.appointmentwin.geometry('1000x800+30+30')
        self.appointmentwin.configure(bg='#E5FFDD')
        self.appointmentwin.resizable(False, False)
        #调用创建treeview的函数
        lst = ['id', 'teacher_name', 'gender', 'province', 'city', 'wchat', 'education', 'school', 'major',
               'teach_time', 'salary', 'teach_year']
        lst_name = ['序号', '讲师姓名', '讲师性别', '省份', '城市', '微信', '最高学历', '毕业院校', '所学专业',
                    '授课时间', '薪水', '教龄']
        self.tv = tv(self.appointmentwin, lst, lst_name)
        self.tv.place(x=30, y=30, width=940, height=500)
        # 读取讲师数据，把讲师数据添加到treeview中
        self.result = query_teacher()
        tv_data(self.tv, self.result)
        # 教员形象照是一个Label标签
        Label(self.appointmentwin,text='教员形象照:',bg='#E5FFDD').place(x=50,y=570,width=100,height=25)
        Button(self.appointmentwin,text='查看',bg='green',fg='white',command=self.show_photo).place(x=160,y=570,width=80,height=40)
        Button(self.appointmentwin, text='预约教员', bg='green', fg='white', command=self.ordered).place(x=250, y=570, width=80,height=40)
        self.appointmentwin.mainloop()

    #预约老师1
    def ordered(self):
        # 先判断是否有选中教员
        iid = self.tv.focus()
        if iid:
            item = self.tv.item(iid)  # item是字典类型
            values = item.get('values')  # values是列表类型
            teacher_id = values[0]  # 讲师id
            # 向订单表中添加数据
            sql = 'insert into t_order (student_id,teacher_id)values (%s,%s)'
            result = service.exec(sql, (student_id, teacher_id))
            if result > 0:
                showinfo('提示', '预约教员成功!')
            else:
                showerror('错误', '预约教员失败，请联系管理员')

        else:
            showerror('错误', '请先选择一位教员，再进行预约')
    #1
    def show_photo(self):
        # 选中哪个讲师，查看哪个讲师的照片
        iid = self.tv.focus()  # 当前的选中行
        if iid:
            item = self.tv.item(iid)  # 选中这行的iid获取了
            values = item.get('values')  # 字典取值，item是字典类型 ，values是列表类型
            photopath = values[12]  # 形象照的路径
            photo2 = PhotoImage(file=photopath)
            # 新建一个窗体，打开形象照
            photowin = Toplevel()
            photowin.geometry('68x109+50+650')
            photowin.resizable(False, False)
            Label(photowin, image=photo2).place(x=0, y=8, width=68, height=109)
            photowin.mainloop()
        else:
            showerror('警告', '请先选择一位讲师再去查看形象照')
    #1
    def get_data(self, event):
        # 获取数据 ，获取id,修改时用，获取评价的内容，填到多行文本框
        iid = self.treev.focus()
        if iid:
            # 根据iid获取选中行数据
            item = self.treev.item(iid)  # item是字典类型
            values = item.get('values')  # 字典取值,values是列表类型
            self.evl_id = values[0]
            self.evl_content = values[3]
            self.evaluation.delete('0.0', END)
            self.evaluation.insert('0.0', self.evl_content)

def query_teacher_id_by_name(teachername):
    sql='select id from t_teacher where teacher_name=%s'
    result= service.query(sql, teachername)
    return result[0][0]

#查询教师姓名
def query_teachername():
    sql='select distinct t.teacher_name from t_teacher as t inner join t_order as o on t.id=o.teacher_id'
    result= service.query2(sql)
    lst=[]
    for item in result:
        lst.append(item[0])
    return lst

def query_teacher():
    sql='select * from vteacher order by id'
    result= service.query2(sql)
    return result

def tv_data(treeview,result): # 向treeview中添加数据
    # 添加数据之前先去检查，treeview中是否有数据
    item_num=treeview.get_children()
    if len(item_num)>0:
        for item in treeview.get_children():
            treeview.delete(item)
    # 向treeview中添加数据
    for item in result:
        treeview.insert('',END,values=item)

def tv(win,lst,lst_name):
    treev=Treeview(win,columns=lst,show='headings')
    for i in range(len(lst)):
        treev.heading(lst[i],text=lst_name[i])
    return treev

def get_id_by_name2(sql,name,gradeid):
    result= service.query(sql, name, gradeid)
    return result[0][0]

def get_id_by_name(sql,name):
    result= service.query(sql, name)
    return result[0][0]

def query_teachmethod():
    sql = 'select teachmethod from t_teachmethod'
    lst = []
    result = service.query2(sql)
    for item in result:
        lst.append(item[0])
    return lst


def query_identity():
    sql='select identity from t_identity'
    result= service.query2(sql)
    lst=[]
    for item in result:
        lst.append(item[0])
    return lst


def query_district():
    sql='select district from t_district'
    result= service.query2(sql)
    lst=[]
    for item in result:
        lst.append(item[0])
    return lst


def query_grade():
    sql = 'select gradename from t_grade'
    lst = []
    result = service.query2(sql)  # result的类型 元组 ((),(),)
    print(result)
    for item in result:
        lst.append(item[0])
    return lst


def get_gradeid_by_name(name):
    sql='select id from t_grade where gradename=%s'
    result= service.query(sql, name)
    return result[0][0]


def get_course_by_grade(id):
    sql = 'select course_name from t_course where grade_id=%s'
    result = service.query(sql, id)
    lst = []
    for item in result:
        lst.append(item[0])
    return lst


# StudentWin()
