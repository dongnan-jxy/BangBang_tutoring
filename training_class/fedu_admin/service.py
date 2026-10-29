"""连接数据库"""
import pymysql
def open():
    db=pymysql.connect(host='127.0.0.1',user='root',password='root',database='fyeducation')
    return db

    #  增删改函数
def exec(sql,values):
    db=open()
    cursor = db.cursor()
    try:
        cursor.execute(sql,values)
        db.commit() #提交
        return 1
    except:
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()

    #带参数查询
def query(sql,*keys):   #*keys位置参数
    db=open()
    cursor = db.cursor()
    cursor.execute(sql,keys)
    result=cursor.fetchall()
    cursor.close()
    db.close()
    return result

    #不带参数查询
def query2(sql):
    db=open()
    cursor = db.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    cursor.close()
    db.close()
    return result

if __name__=='__main__':
    sql = 'select*from t_teacher'
    result = query2(sql)
    print(result)