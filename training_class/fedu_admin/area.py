#coding:utf-8
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview
import service
adminmainobj=None
class AreaWin():
    def __init__(self,insert,update,delete,query):
        self.areawin = Toplevel()
        self.areawin.title('邦邦培训-后台管理系统')
        self.areawin.geometry('350x250+600+200')
        self.areawin.configure(bg='#E5FFDD')
        self.areawin.resizable(False, False)
        img=PhotoImage(file='./images/admin-bg.png')
        Label(self.areawin,image=img).place(x=0,y=0,width=350,height=250)
        # 页面布局
        Label(self.areawin, text='所属省份:', bg='#E5FFDD').place(x=20, y=20, width=80, height=25)
        self.province = Entry(self.areawin)
        self.province.place(x=110, y=20, width=200, height=25)

        Label(self.areawin, text='所属城市:', bg='#E5FFDD').place(x=20, y=55, width=80, height=25)
        self.city = Entry(self.areawin)
        self.city.place(x=110, y=55, width=200, height=25)

        # TreeView对象
        lst = ['id', 'province', 'city']
        lst_name = ['序号', '省份', '城市']
        self.tv = tv(self.areawin, lst, lst_name)
        self.tv.place(x=20, y=90, width=300, height=100)
        self.querypro()  # 调用查询的方法
        self.tv.bind('<Double-Button-1>', self.get_selected_item_data)
        # 四个按钮
        self.insertbtn = Button(self.areawin, text='添加', bg='green', fg='white', command=self.insertpro)
        self.insertbtn.place(x=30, y=200, width=60, height=40)

        self.updatabtn = Button(self.areawin, text='修改', bg='green', fg='white', command=self.modifypro)
        self.updatabtn.place(x=100, y=200, width=60, height=40)

        self.deletebtn = Button(self.areawin, text='删除', bg='green', fg='white', command=self.deletepro)
        self.deletebtn.place(x=170, y=200, width=60, height=40)

        self.querybtn = Button(self.areawin, text='查询', bg='green', fg='white', command=self.querypro)
        self.querybtn.place(x=240, y=200, width=60, height=40)
        # 判断按钮的启用和禁用状态
        if insert == True:
            self.insertbtn.configure(state=NORMAL)  # 按钮启动
            self.updatabtn.configure(state=DISABLED)  # 按钮禁 用
            self.deletebtn.configure(state=DISABLED)
            self.querybtn.configure(state=DISABLED)
        elif update == True:
            self.insertbtn.configure(state=DISABLED)
            self.updatabtn.configure(state=NORMAL)
            self.deletebtn.configure(state=DISABLED)
            self.querybtn.configure(state=DISABLED)
        elif delete == True:
            self.insertbtn.configure(state=DISABLED)
            self.updatabtn.configure(state=DISABLED)
            self.deletebtn.configure(state=NORMAL)
            self.querybtn.configure(state=DISABLED)
        elif query == True:
            self.insertbtn.configure(state=DISABLED)
            self.updatabtn.configure(state=DISABLED)
            self.deletebtn.configure(state=DISABLED)
            self.querybtn.configure(state=NORMAL)
            # 当前窗体关闭时，主窗体显示
        self.areawin.bind('<Destroy>', self.on_toplevel_close)
        self.areawin.mainloop()

    #
    def deletepro(self):
        iid = self.tv.focus()
        if iid:
            item = self.tv.item(iid)
            values = item.get('values')  # 根据key获取值,values是列表类型
            self.area_id = values[0]
            # 删除不需判断是否为空，但是删除时要注意主外键关系，如果该省份城市被其它表引用，将子表中的数据也需要删除
            # 在这里没有验证（同学可自行验证，参考《E起去旅行》）
            sql = 'delete from t_area where id =%s'
            result = service.exec(sql, self.area_id)
            if result > 0:
                showinfo('提示', '删除省份城市成功')
                self.areawin.destroy()  # 当前窗口关闭
                adminmainobj.adminwin.deiconify()  # 主窗口显示
            else:
                showerror('错误', '删除省份城市失败')
        else:
            showerror('错误', '请先选择一条要删除的数据')

    def get_selected_item_data(self, event):
        iid = self.tv.focus()  # iid是字符串类型
        print(iid, type(iid))
        if iid:  # 利用到了对象的布尔值，非空的字符串结果为True
            item = self.tv.item(iid)
            values = item.get('values')  # values是列表类型
            self.province.delete(0, END)
            self.city.delete(0, END)
            self.province.insert(0, values[1])  # 省份
            self.city.insert(0, values[2])

        # 添加省份
    def insertpro(self):
        province = self.province.get()
        city = self.city.get()
        if province == '' or city == '':
            showerror('警告', '所属于省份和所属城市不能为空')
            return False
        else:
            sql = 'insert into t_area(province,city) values(%s,%s)'  # 执行添加操作
            result = service.exec(sql, (province, city))
            if result > 0:
                showinfo('提示', '添加省份和城市成功')
                # 当前窗体关闭
                self.areawin.destroy()
                adminmainobj.adminwin.deiconify()  # 主窗口显示
            else:
                showerror('错误', '添加省份和城市失败')

        # 修改省份
    def modifypro(self):
        iid = self.tv.focus()  # iid是字符串类型
        if iid:
            item = self.tv.item(iid)
            values = item.get('values')
            self.area_id = values[0]
            if self.province.get() == '' or self.city.get() == '':
                showerror('警告', '所属省份和所属城市不能为空')
                return False
            else:
                sql = 'update t_area set province=%s,city=%s where id=%s'
                result = service.exec(sql, (self.province.get(), self.city.get(), self.area_id))
                if result > 0:
                    showinfo('提示', '修改省份和城市成功')
                    self.areawin.destroy()
                    adminmainobj.adminwin.deiconify()
                else:
                    showerror('错误', '修改省份和城市失败')
        else:
            showerror('警告', '请先选择一条要修改的数据')

    def querypro(self):
        # 根据省份查
        # 根据城市查
        # 根据省份和城市查
        # 查询全部
        # result=((),)
        if self.province.get() == '' and self.city.get() == '':
            sql = 'select * from t_area'
            result = service.query2(sql)
        elif self.province.get() != '' and self.city.get() == '':
            sql = 'select * from t_area where province like %s'
            result = service.query(sql, '%' + self.province.get() + '%')
        elif self.city.get() != '' and self.province.get() == '':
            sql = 'select * from t_area where city=%s'
            result = service.query(sql, self.city.get())

        else:
            # 根据省份和城市 可以精确也可以模糊
            sql = 'select * from t_area where province=%s and  city=%s'
            result = service.query(sql, self.province.get(), self.city.get())
        tv_data(self.tv, result)

    def on_toplevel_close(self, event):
        self.areawin.destroy()
        adminmainobj.adminwin.deiconify()


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

