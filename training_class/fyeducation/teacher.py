from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview

objmain = None  # 代表主窗口登录窗口
teacher_id = 1
teacher_pwd = ""
from training_class.fyeducation import service


class TeacherWin():
    def __init__(self):
        self.win = Toplevel()
        self.win.title('邦邦培训班-教师端')
        self.win.geometry('1500x900+0+0')
        self.win.config(bg='#E5FFDD')
        self.win.resizable(width=False, height=False)
        self.img = PhotoImage(file='images/teacherbj.png')
        Label(self.win, image=self.img).place(x=0, y=0, width=1500, height=980)
        # 个人中心内容，三个Label，六个按钮
        Label(self.win, text='简历更新', bg='#E5FFDD', font=('宋体', 16)).place(x=400, y=110, width=80, height=20)
        # 四个Button
        Button(self.win, text='我的信息', bg='green', font=('宋体', 16), fg='white', command=self.myinfo).place(x=400,
                                                                                                                y=150,
                                                                                                                width=100,
                                                                                                                height=40)
        Button(self.win, text='修改信息', bg='green', font=('宋体', 16), fg='white',command=self.modifyinfo).place(x=510, y=150,
                                                                                           width=100,
                                                                                           height=40)
        Button(self.win, text='修改密码', bg='green', font=('宋体', 16), fg='white', command=self.updatepwd).place(
            x=400, y=200,
            width=100,
            height=40)
        Button(self.win, text='完善信息', bg='green', font=('宋体', 16), fg='white', command=self.infomation).place(
            x=510, y=200,
            width=100,
            height=40)

        Label(self.win, text='培训情况', bg='#E5FFDD', font=('宋体', 16)).place(x=400, y=270, width=100, height=20)
        Button(self.win, text='预约我的培训', bg='green', font=('宋体', 10), fg='white',command=self.ordered).place(x=400, y=300,
                                                                                               width=100,
                                                                                               height=40)
        Button(self.win, text='学员评价', bg='green', font=('宋体', 16), fg='white',command=self.showevl).place(x=510, y=300,
                                                                                           width=100,
                                                                                           height=40)
        # 如何快速找到家教
        self.infoimg = PhotoImage(file='images/info.png')
        Label(self.win, image=self.infoimg).place(x=650, y=110, width=750, height=375)

        # 当点击关闭时，显示隐藏的窗口
        self.win.bind('<Destroy>', self.on_toplevel_close)
        self.win.mainloop()

    #预约我的家教
    def ordered(self):
        orderedwin = Toplevel()
        orderedwin.geometry('400x300+600+300')
        orderedwin.title('邦邦培训·-教员端-查看预约我的家教')
        orderedwin.resizable(False, False)
        orderedwin.configure(bg='#E5FFDD')
        sql="select  o.id,s.student_name,s.gender,s.address,s.wchat from t_order as o inner join t_student as s on s.id=o.student_id where o.teacher_id=%s and s.student_name!=''"
        result= service.query(sql, teacher_id)
        lst=['id','student_name','gender','address','wchat']
        lst_name=['序号','学生姓名','性别','地址','微信']
        self.ordertv=tv(orderedwin,lst,lst_name)
        self.ordertv.place(x=15,y=20,width=370,height=150)
        tv_data(self.ordertv,result)
        Button(orderedwin,text='返回',fg='white',bg='green',command=orderedwin.destroy).place(x=150,y=200,width=60,height=40)

        orderedwin.mainloop()

    #显示学生的评价
    def showevl(self):
        showevlwin=Toplevel()
        showevlwin.geometry('400x300+600+300')
        showevlwin.title('邦邦培训-教师端-查看学员评价')
        showevlwin.resizable(False, False)
        showevlwin.configure(bg='#E5FFDD')
        #Treeview展示数据
        lst=['id','student_name','content']
        lst_name=['序号','学生姓名','评价内容']
        self.showevltv=tv(showevlwin,lst,lst_name)
        self.showevltv.place(x=15,y=20,width=370,height=200)
        # 向Treeview中添加数据
        sql='select e.id,s.student_name,e.content from t_evaluation as e inner join t_student as s on s.id=e.student_id where teacher_id=%s'
        result= service.query(sql, teacher_id)
        tv_data(self.showevltv,result)
        # 返回按钮
        Button(showevlwin,text='返回',bg='green',fg='white',command=showevlwin.destroy).place(x=200,y=250,width=60,height=40)
        showevlwin.mainloop()

    # 清空登录信息
    def on_toplevel_close(self, event):
        objmain.loginwin.deiconify()
        objmain.entry_user.delete(0, END)
        objmain.entry_pwd.delete(0, END)

    def updatepwd(self):
        # 先去打开修改密码窗体
        self.updatetk = Toplevel()
        self.updatetk.title('云朵家教-教员端-修改密码')
        self.updatetk.geometry('388x290+600+200')
        self.updatetk.resizable(False, False)
        self.updatetk.configure(bg='#E5FFDD')
        img = PhotoImage(file='images/changepwd.png')
        Label(self.updatetk, image=img).place(x=0, y=0, width=388, height=290)
        # 三个单行文本框
        self.oldpwd = Entry(self.updatetk, show='*')
        self.oldpwd.insert(0, teacher_pwd)
        self.oldpwd.config(state='readonly')
        self.oldpwd.place(x=120, y=90, width=200, height=20)
        # 新密码
        self.newpwd = Entry(self.updatetk, show='*')
        self.newpwd.place(x=120, y=120, width=200, height=20)
        # 确认密码
        self.conpwd = Entry(self.updatetk, show='*')
        self.conpwd.place(x=120, y=155, width=200, height=20)
        # 两个键钮
        Button(self.updatetk, text='修改', bg='green', fg='white', font=('宋体', 16), command=self.changepwd).place(
            x=180, y=195,
            width=60,
            height=25)
        Button(self.updatetk, text='取消', bg='green', fg='white', font=('宋体', 16),
               command=self.updatetk.destroy).place(x=250,
                                                    y=195,
                                                    width=60,
                                                    height=25)

        self.updatetk.mainloop()

    def changepwd(self):
        if self.newpwd.get() == '' or self.conpwd.get() == '':
            showerror('警告', '新密码与确认密码不能为空')
            return False
        if self.newpwd.get() != self.conpwd.get():
            showerror('警告', '新密码与确认密码不同')
        else:
            # 修改密码操作
            sql = 'update t_teacher set pwd=%s where id=%s'
            result = service.exec(sql, (self.newpwd.get(), teacher_id))
            if result > 0:
                showinfo("提示", '密码修改成功，下次登录时起作用')
                self.updatetk.destroy()
            else:
                showinfo("错误", '修改密码失败')

    # 完善信息函数
    def infomation(self):
        self.infowin = Toplevel()
        self.infowin.title('云朵家教-教员端-完善个人信息')
        self.infowin.geometry('800x600+300+50')
        self.infowin.configure(bg='#E5FFDD')
        self.infowin.resizable(False, False)  # 不允许调整窗体的大小
        img = PhotoImage(file='images/information.png')
        Label(self.infowin, image=img).place(x=40, y=20, width=596, height=495)
        # # 在窗体上放置组件，页面布局
        # # 讲师姓名
        self.name = Entry(self.infowin)
        self.name.place(x=170, y=95, width=200, height=25)
        # # 讲师性别
        self.genderv = IntVar()
        self.genderv.set(1)  # 1表示的是男
        self.rdgender1 = Radiobutton(self.infowin, text='男', bg='#E5FFDD', variable=self.genderv, value=1)
        self.rdgender2 = Radiobutton(self.infowin, bg='#E5FFDD', text='女', variable=self.genderv, value=0)
        self.rdgender1.place(x=170, y=130, width=60, height=25)
        self.rdgender2.place(x=240, y=130, width=60, height=25)
        # # 出生年月
        self.birthday = Entry(self.infowin)
        self.birthday.place(x=170, y=170, width=200, height=25)
        # # 省份 从数据库中读取省份
        self.lst_pro = querypro()  # 调用函数
        self.v = StringVar()
        self.v.set(self.lst_pro[0])  # 默认选中组合框中的第一个
        self.province = Combobox(self.infowin, values=self.lst_pro, textvariable=self.v)
        self.province.place(x=170, y=205, width=120, height=25)
        # # 微信
        self.wchat = Entry(self.infowin)
        self.wchat.place(x=170, y=240, width=200, height=25)
        # # 家庭住址
        self.address = Entry(self.infowin)
        self.address.place(x=170, y=275, width=200, height=25)
        # # 所属区域
        self.lst_dis = query_district()
        self.districtv = StringVar()
        self.districtv.set(self.lst_dis[0])
        self.district = Combobox(self.infowin, values=self.lst_dis, textvariable=self.districtv)
        self.district.place(x=170, y=315, width=120, height=25)
        # # 最高学历
        self.lst_edu = query_education()
        self.educationv = StringVar()
        self.educationv.set(self.lst_edu[1])
        self.education = Combobox(self.infowin, values=self.lst_edu, textvariable=self.educationv)
        self.education.place(x=170, y=350, width=120, height=25)
        # # 毕业院校
        self.school = Entry(self.infowin)
        self.school.place(x=170, y=390, width=200, height=25)
        # # 教员身份
        self.lst_identity = query_identity()
        self.identityv = StringVar()
        self.identityv.set(self.lst_identity[0])
        self.identity = Combobox(self.infowin, values=self.lst_identity, textvariable=self.identityv)
        self.identity.place(x=170, y=425, width=120, height=25)
        # # 所学专业
        self.major = Entry(self.infowin)
        self.major.place(x=170, y=465, width=200, height=25)
        # # 授课时间
        t_time = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        t_time2 = ['上午', '下午', '晚上']
        self.teach_timev1 = StringVar()
        self.teach_timev1.set(t_time[0])  # 默认是星期一
        self.teach_time1 = Combobox(self.infowin, values=t_time, textvariable=self.teach_timev1)
        self.teach_time1.place(x=550, y=95, width=100, height=25)
        #
        self.teach_timev2 = StringVar()
        self.teach_timev2.set(t_time2[0])  # 默认是星期一
        self.teach_time2 = Combobox(self.infowin, values=t_time2, textvariable=self.teach_timev2)
        self.teach_time2.place(x=660, y=95, width=100, height=25)
        # # 期望的上课薪酬
        self.salary = Spinbox(self.infowin, from_=60, to=120, increment=10)
        self.salary.place(x=550, y=130, width=140, height=25)
        Label(self.infowin, text='元/时', bg='#E5FFDD').place(x=690, y=130, width=60, height=25)
        # # 授课方式
        self.lst_teach_method = query_teachmethod()
        self.teach_methodv = StringVar()
        self.teach_methodv.set(self.lst_teach_method[0])
        self.teach_method = Combobox(self.infowin, values=self.lst_teach_method, textvariable=self.teach_methodv)
        self.teach_method.place(x=550, y=165, width=120, height=25)
        # # 所获证书
        self.certifications = Entry(self.infowin)
        self.certifications.place(x=550, y=205, width=200, height=25)
        # # 教龄
        self.teach_year = Spinbox(self.infowin, from_=1, to=30)
        self.teach_year.place(x=550, y=240, width=140, height=25)
        Label(self.infowin, text='年', bg='#E5FFDD').place(x=690, y=240, width=60, height=25)
        # # 经验  #Text多行文本框
        self.experience = Text(self.infowin)
        self.experience.place(x=550, y=280, width=200, height=65)
        # # 自我介绍
        self.introduce = Text(self.infowin)
        self.introduce.place(x=550, y=355, width=200, height=95)
        # #  上传照片
        self.path = Entry(self.infowin)
        self.path.place(x=550, y=460, width=120, height=25)
        Button(self.infowin, text='上传照片', bg='green', fg='white', command=self.upload).place(x=680, y=460, width=60,
                                                                                                 height=25)
        # # 确定按钮和取消按钮
        Button(self.infowin, text='确定', bg='green', fg='white', command=self.updateinfo).place(x=450, y=520, width=60,
                                                                                                 height=25)
        Button(self.infowin, text='取消', bg='green', fg='white', command=self.infowin.destroy).place(x=520, y=520,
                                                                                                      width=60,
                                                                                                      height=25)

        self.infowin.mainloop()

        def upload(self): # 点击上传照片按钮时执行，打开文件对话框
            b=askopenfile(title='选择形象照',filetypes=[('图片文件','*.png')])
            self.path.delete(0,END) # 存储图片路径的文本框，先将值清空
            self.path.insert(0,b.name) # b.name是文件的完整咱径
    def upload(self):
        b = askopenfile(title='选择形象照', filetypes=[('图片文件', '*.png')])
        self.path.delete(0, 'end')
        self.path.insert(0, b.name)

    def updateinfo(self):  # 确定按钮调用的方法
        # 获取值
        name = self.name.get()  # 获取讲师的姓名
        gender = '男' if self.genderv.get() == 1 else '女'
        brithday = self.birthday.get()  # 出生年月的
        #         # 省份  查询，根据值去查询对应省份的id
        #         # province是什么类型?
        province = get_id('select id from t_area where province=%s and city=%s', self.v.get().split('-'))
        wchat = self.wchat.get()  # 获取微信， 单行文本框
        address = self.address.get()  # 获取家庭住址，单行文本框
        # 所属区域是外键， 根据名称到区域表中查询id
        district = get_id('select id from t_district where district=%s', self.districtv.get())
        # 最高学历是外键，根据学历的名称到学历表中查询id
        education = get_id('select id  from t_education where education=%s', self.educationv.get())
        school = self.school.get()  # 毕业院校，单行文本框
        # 教员身份是外键，根据教员的身份名称到身份表中查询id
        identity = get_id('select id from t_identity where identity=%s', self.identityv.get())
        # 所学专业
        major = self.major.get()  # 所学专业的单行文本框
        # 授课时间是两个组合框，   两个组合框中的值  使用空格连接成一个字符串
        teach_time = self.teach_timev1.get() + ' ' + self.teach_timev2.get()
        # 期望薪酬
        salary = int(self.salary.get())
        # 授课方式外键，根据授课方式到授课方式表中查询id
        teach_method = get_id('select id from t_teachmethod where teachmethod=%s', self.teach_methodv.get())
        # 所获证书
        certifications = self.certifications.get()  # 单行文本框
        # 教龄
        teach_year = int(self.teach_year.get())
        # 经验,经验是一个多行文本框
        experience = self.experience.get('0.0', END)
        # 自我介绍
        introduce = self.introduce.get('0.0', END)
        # 照片的路径
        photo = self.path.get()  # 获取单行文本框的值
        # 编写sql语句
        sql = 'update t_teacher set teacher_name=%s,gender=%s,birthday=%s,province=%s,wchat=%s,address=%s,district_id=%s,highest_education_id=%s,school=%s,identity_id=%s,major=%s,teach_time=%s,salary=%s,teach_method_id=%s,certifications=%s,teach_year=%s,experience=%s,introduce=%s,photo=%s where id=%s'
        result = service.exec(sql, (name, gender, brithday,
                                    province, wchat, address, district, education,
                                    school, identity, major, teach_time,
                                    salary, teach_method, certifications,
                                    teach_year, experience, introduce, photo,
                                    teacher_id))
        if result > 0:
            showinfo('提示', '信息完善，提交成功')
            # 直接关闭当前窗口
            self.infowin.destroy()
        else:
            showerror('错误', '信息完善出错，请联系管理员')

    # 查询个人信息功能
    def myinfo(self):
        # 先去判断，什么情况下显示个人信息，当信息被完善之后显示个人信息
        sql = 'select teacher_name from t_teacher where id=%s'  # 如果姓名存在就显示信息，否则先完善信息
        result = service.query(sql, teacher_id)
        if result[0][0] == None:
            showinfo('提示', '请先完善个人信息')
        # 展示个人信息
        else:
            wininfo = Toplevel()
            wininfo.title('邦邦培训班-教师端-显示个人信息')
            wininfo.geometry('800x600+300+50')
            wininfo.config(bg='#E5FFDD')
            wininfo.resizable(width=False, height=False)
            image = PhotoImage(file='images/showinfo.png')
            Label(wininfo, image=image).place(x=40, y=20, width=594, height=467)

            #查询个人信息
            teacherinfo = read_info()
            #姓名
            Label(wininfo, text=teacherinfo[0], bg='#E5FFDD',font=('宋体',16)).place(x=170, y=95, width=60, height=25)
            #性别
            Label(wininfo,text=teacherinfo[1], bg='#E5FFDD',font=('宋体',16)).place(x=170, y=130, width=60, height=25)
            #出生年月
            Label(wininfo,text=str(teacherinfo[2]).split(' ')[0], bg='#E5FFDD',font=('宋体',16)).place(x=170, y=162, width=120, height=25)
            #住址
            province = get_value_by_id('select province from t_area where id=%s', teacherinfo[3])
            city = get_value_by_id('select city from t_area where id=%s', teacherinfo[3])
            Label(wininfo, text=province + '-' + city, bg='#E5FFDD', font=('宋体',14)).place(x=170, y=200, width=120, height=25)
            # 微信
            Label(wininfo,text=teacherinfo[4], bg='#E5FFDD',font=('宋体',16)).place(x=170, y=235, width=100, height=25)
            #家庭住址
            Label(wininfo,text=teacherinfo[5], bg='#E5FFDD',font=('宋体',16)).place(x=170, y=270, width=150, height=25)
            #所属区域
            distict = get_value_by_id(
                'select district from t_district where id=%s', teacherinfo[6])
            Label(wininfo,text=distict, bg='#E5FFDD',font=('宋体',16)).place(x=170, y=305, width=60, height=25)
            # 学历
            education=get_value_by_id(
                'select education from t_education where id=%s', teacherinfo[7])
            Label(wininfo,text=education, bg='#E5FFDD',font=('宋体',16)).place(x=170, y=340, width=60, height=25)
            # 毕业院校
            Label(wininfo, text=teacherinfo[8], bg='#E5FFDD', font=('宋体',16)).place(x=170, y=375, width=150, height=25)
            # 教员身份，是外键，根据id到教员身份表中查询身份的名称
            identity = get_value_by_id('select identity from t_identity where id=%s', teacherinfo[9])
            Label(wininfo, text=identity, bg='#E5FFDD', font=('宋体',16)).place(x=170, y=410, width=100, height=25)
            # 所学专业
            Label(wininfo, text=teacherinfo[10], bg='#E5FFDD', font=('宋体',16)).place(x=170, y=445, width=100, height=25)
            # 右侧部分
            # 授课时间
            Label(wininfo, text=teacherinfo[11], bg='#E5FFDD', font=('宋体',16)).place(x=490, y=200, width=130, height=25)
            # 授课薪酬
            Label(wininfo, text=str(teacherinfo[12]) + '元/时', bg='#E5FFDD', font=('宋体',16)).place(x=490, y=235, width=150,
                                                                                             height=25)
            # 授课方式是外键，根据id到授课方式表中查询授课方式
            teachmethod = get_value_by_id('select teachmethod from t_teachmethod where id=%s', teacherinfo[13])
            Label(wininfo, text=teachmethod, bg='#E5FFDD', font=('宋体',16)).place(x=490, y=270, width=90, height=25)
            # 所获证书
            Label(wininfo, text=teacherinfo[14], bg='#E5FFDD', font=('宋体',16)).place(x=490, y=305, width=90, height=25)
            # 教年
            Label(wininfo, text=str(teacherinfo[15]) + '年', bg='#E5FFDD', font=('宋体',16)).place(x=490, y=340, width=90,
                                                                                          height=25)
            # 经验和自我介绍都是多行文本框
            ex = Text(wininfo, bg='#E5FFDD', bd=0, font=('宋体',16))
            ex.insert('0.0', teacherinfo[16])
            ex.place(x=490, y=380, width=250, height=60)
            # 自我介绍
            intro = Text(wininfo, bg='#E5FFDD', bd=0, font=('宋体',16))
            intro.insert('0.0', teacherinfo[17])
            intro.place(x=490, y=450, width=250, height=60)
            # 显示个人形象照
            image2 = PhotoImage(file=teacherinfo[18])
            Label(wininfo, image=image2).place(x=380, y=80, width=68, height=109)
            # 按回按钮
            Button(wininfo, text='返回', bg='green', fg='white', command=wininfo.destroy).place(x=400, y=530, width=60,
                                                                                                height=25)

            wininfo.mainloop()

    #修稿个人信息
    def modifyinfo(self):
        modiwin = Toplevel()
        modiwin.geometry('800x600+300+100')
        modiwin.title('邦邦培训-教师端-修改个人信息')
        modiwin.resizable(False, False)
        modiwin.configure(background='#E5FFDD')

        #加载图片
        image33=PhotoImage(file='images/information2.png')
        Label(modiwin,image=image33).place(x=40,y=20,width=594,height=467)
        #开始读取数据
        result = read_info()
        self.name=Entry(modiwin)
        self.name.place(x=170,y=80,width=200,height=25)
        self.name.insert(0,result[0])

        #性别，单选按钮
        self.genderv=IntVar()
        self.genderv.set(1 if result[1]=='男' else 0)
        self.rdgender1=Radiobutton(modiwin,text='男',variable=self.genderv,value=1,bg='#E5FFDD')
        self.rdgender2=Radiobutton(modiwin,text='女',variable=self.genderv,value=0,bg='#E5FFDD')
        self.rdgender1.place(x=170,y=115,width=60,height=25)
        self.rdgender2.place(x=240,y=115,width=60,height=25)
        #出生年月
        self.birthday=Entry(modiwin)
        self.birthday.place(x=170,y=150,width=200,height=25)
        self.birthday.insert(0,str(result[2]).split(' ')[0])
        #省份  两个拼接
        province = get_value_by_id('select province from t_area where id=%s',result[3])
        city = get_value_by_id('select city from t_area where id=%s',result[3])
        self.v = StringVar()
        self.v.set(province+'-'+city)
        self.lst_pro=querypro()   #查询省份中所有数据，加载到组合框中
        self.province=Combobox(modiwin,textvariable=self.v,values=self.lst_pro)
        self.province.place(x=170,y=190,width=200,height=25)
        #微信
        self.wchat=Entry(modiwin)
        self.wchat.place(x=170,y=223,width=200,height=25)
        self.wchat.insert(0,result[4])
        #家庭住址
        self.address=Entry(modiwin)
        self.address.place(x=170,y=263,width=200,height=25)
        self.address.insert(0,result[5])
        #区域
        district = get_value_by_id(
            'select district from t_district where id=%s',result[6])
        self.districtv=StringVar()
        self.districtv.set(district)
        self.lst_dis=query_district()   #查询所有区域绑定组合框中
        self.district=Combobox(modiwin,textvariable=self.districtv,values=self.lst_dis)
        self.district.place(x=170,y=303,width=200,height=25)
        #最高学历
        education = get_value_by_id('select education from t_education where id=%s',result[7])
        self.educationv=StringVar()
        self.educationv.set(education)
        self.lst_edu=query_education()       #查询学历表中所有数据
        self.education=Combobox(modiwin,textvariable=self.educationv,values=self.lst_edu)
        self.education.place(x=170,y=338,width=200,height=25)
        #毕业院校
        self.school = Entry(modiwin)
        self.school.place(x=170,y=373,width=200,height=25)
        self.school.insert(0,result[8])
        #教师身份
        identity = get_value_by_id('select identity from t_identity where id=%s', result[9])
        self.identityv=StringVar()
        self.identityv.set(identity)
        self.lst_identity=query_identity()
        self.identity=Combobox(modiwin,textvariable=self.identityv,values=self.lst_identity)
        self.identity.place(x=170,y=410,width=200,height=25)
        #所学专业
        self.major=Entry(modiwin)
        self.major.place(x=170,y=445,width=200,height=25)
        self.major.insert(0,result[10])
        #授课时间
        t_time = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        t_time2 = ['上午', '下午', '晚上']
        self.teach_timev1 = StringVar()
        self.teach_timev1.set(result[11].split(' ')[0])
        self.teach_time1 = Combobox(modiwin, values=t_time, textvariable=self.teach_timev1)
        self.teach_time1.place(x=550, y=80, width=100, height=25)

        self.teach_timev2 = StringVar()
        self.teach_timev2.set(result[11].split(' ')[1])
        self.teach_time2 = Combobox(modiwin, values=t_time2, textvariable=self.teach_timev2)
        self.teach_time2.place(x=660, y=80, width=100, height=25)
        #授课薪酬
        self.salary = Spinbox(modiwin,from_=60,to=120,increment=10)
        self.salary.place(x=550,y=115,width=140,height=25)
        self.salary.setvar(str(result[12]))
        Label(modiwin,text='元/时',bg='#E5FFDD').place(x=690,y=115,width=60,height=25)
        #授课方式
        teach_method = get_value_by_id('select teachmethod from t_teachmethod where id=%s',result[13])
        self.teach_methodv=StringVar()
        self.teach_methodv.set(teach_method)
        self.lst_teach_method=query_teachmethod()
        self.teach_method=Combobox(modiwin,textvariable=self.teach_methodv,values=self.lst_teach_method)
        self.teach_method.place(x=550,y=150,width=100,height=25)
        #所获证书
        self.certifications=Entry(modiwin)
        self.certifications.place(x=550,y=185,width=200,height=25)
        self.certifications.insert(0,result[14])
        #教龄
        self.teach_year = Spinbox(modiwin,from_=1,to=30,increment=1)
        self.teach_year.setvar(str(result[15]))
        self.teach_year.place(x=550,y=220,width=100,height=25)
        Label(modiwin,text='年',bg='#E5FFDD').place(x=680,y=220,width=50,height=25)
        #经验
        self.experience=Text(modiwin)
        self.experience.place(x=550,y=260,width=200,height=65)
        self.experience.insert('0.0',result[16])
        #自我介绍
        self.introduce = Text(modiwin)
        self.introduce.place(x=550,y=345,width=200,height=65)
        self.introduce.insert('0.0',result[17])
        #上传照片
        self.path=Entry(modiwin)
        self.path.place(x=550,y=455,width=120,height=25)
        self.path.insert(0,result[18])
        Button(modiwin,text='上传照片',bg='green',fg='white',command=self.upload).place(x=680,y=455,width=60,height=25)
        #确定和取消
        Button(modiwin, text='确定', bg='green', fg='white', command=self.updateinfo).place(x=450, y=520, width=60,
                                                                                            height=25)
        Button(modiwin, text='取消', bg='green', fg='white', command=modiwin.destroy).place(x=520, y=520, width=60,height=25)

        modiwin.mainloop()

def get_value_by_id(sql,id): # 根据id查询名称
    result= service.query(sql, id)
    return result[0][0]

def get_id(sql, name):
    if isinstance(name, list):  ## 判断 name的类型，如果是列表类型，说明提省份t_area表
        result = service.query(sql, name[0], name[1])
    else:
        result = service.query(sql, name)
    return result[0][0]


# # pro是省份的简写
def querypro():  # pro是省份的简写
    sql = 'select * from t_area'
    result = service.query2(sql)  # ((1,吉林省,吉林市))
    lst_pro = []
    for item in result:
        lst_pro.append(item[1] + '-' + item[2])
    return lst_pro


## 查询区域
def query_district():
    sql = 'select * from t_district'
    result = service.query2(sql)
    lst_dis = []
    for item in result:
        lst_dis.append(item[1])
    return lst_dis


# 查询学历
def query_education():
    sql = 'select * from t_education'
    result = service.query2(sql)
    lst_edu = []
    for item in result:
        lst_edu.append(item[1])
    return lst_edu


# 查询教员身份
def query_identity():
    sql = 'select * from t_identity'
    result = service.query2(sql)
    lst_identity = []
    for item in result:
        lst_identity.append(item[1])
    return lst_identity


# 哪个身份上门
def query_teachmethod():
    sql = 'select * from t_teachmethod'
    result = service.query2(sql)
    lst_teach_metho = []
    for item in result:
        lst_teach_metho.append(item[1])
    return lst_teach_metho

#查询
def read_info():
    sql='select teacher_name,gender,birthday,province,wchat,address,district_id,highest_education_id,school,identity_id,major,teach_time,salary,teach_method_id,certifications,teach_year,experience,introduce,photo from t_teacher where id=%s'
    result= service.query(sql, teacher_id)
    # result是元组类型((),)
    return result[0]

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

# TeacherWin()
