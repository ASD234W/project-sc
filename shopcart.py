from dbconfig import conn, cur

def getList():
    sql="select Pid, Name,Description, Quantity,Price from shoppingcart where Quantity>0;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def addcart(Pid,number):
    sql="INSERT INTO customercart(Pid, Name, Description, Price) select Pid,Name,Description,Price from shoppingcart where Pid = %s;"
    cur.execute(sql,(Pid,))
    conn.commit()
    
    sql = "update customercart set Quantity =Quantity + %s where Pid = %s;"
    cur.execute(sql,(number,Pid))
    conn.commit()
    
    sql = "update shoppingcart set Quantity = Quantity - %s where Pid = %s;"
    cur.execute(sql,(number,Pid))
    conn.commit()
    return True

def delcart(Pid, number):
    sql="update customercart set Quantity =Quantity - %s where Pid = %s;"
    cur.execute(sql,(number,Pid))
    conn.commit()
    
    sql="delete from customercart where Quantity = 0;"
    cur.execute(sql)
    conn.commit()
    
    sql="update shoppingcart set Quantity =Quantity + %s where Pid = %s;"
    cur.execute(sql,(number,Pid))
    conn.commit()
    return True

def listcart():
    sql="select Pid, Name,Description, Quantity,Price from customercart where Quantity>0;"
    cur.execute(sql)
    records = cur.fetchall()
    return records


def SFinish():
    sql="select sum(Quantity*Price) as toal from customercart where Quantity>0;"
    cur.execute(sql)
    record = cur.fetchone()
    return record
    
    sql="Truncate Table customercart;"
    cur.execute(sql)
    conn.commit()
    return

def goodslist():
    sql="select Pid, Name,Description, Quantity,Price from shoppingcart;"
    cur.execute(sql)
    records = cur.fetchall()
    return records


def addgoods(name,des,number,price):
    sql="insert into shoppingcart (Name,Description,Quantity,Price) values (%s,%s,%s,%s);"
    cur.execute(sql,(name,des,number,price))
    conn.commit()
    return True


def delgoods(Pid):
    sql="delete from shoppingcart where Pid=%s;"
    cur.execute(sql,(Pid,))
    conn.commit()
    return True

def changegoods(Pid,name,des,number,price):
    sql="update shoppingcart set Name=%s, Description=%s, Quantity=%s, Price=%s where Pid=%s;"
    cur.execute(sql,(name,des,number,price,Pid))
    conn.commit()
    return True

def addgoodsN(Pid,number):
    sql="update shoppingcart set Quantity=Quantity+%s where Pid=%s;"
    cur.execute(sql,(number,Pid))
    conn.commit()
    return True

