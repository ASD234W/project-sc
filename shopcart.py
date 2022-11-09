from dbconfig import conn, cur

def getList():
    sql="select Pid, Name,Description, Quantity,Price from shoppingcart where Quantity>0;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def addcart(Pid,number):
    sql="INSERT INTO customercart(Pid, Name, Description, Price) select Pid,Name,Description,Price from shoppingcart where Pid = %s and Pid NOT IN (select Pid from customercart);"
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
    sql="update shoppingcart set Quantity =Quantity + (select if(Quantity>%s,%s,Quantity) from customercart where Pid = %s) where Pid = %s and Pid IN (select Pid from customercart);"
    cur.execute(sql,(number,number,Pid,Pid))
    conn.commit()
    
    sql="delete from customercart where Quantity <= 0;"
    cur.execute(sql)
    conn.commit()
    
    sql="update customercart set Quantity =Quantity - if(Quantity>%s,%s,Quantity) where Pid = %s and Pid IN (select Pid from customercart);"
    cur.execute(sql,(number,number,Pid))
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
    
    sql="Truncate Table customercart;"
    cur.execute(sql)
    conn.commit()
    return record

def goodslist():
    sql="select Pid, Name,Description, Quantity,Price from shoppingcart;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def showgood(Pid):
    sql="select Pid, Name,Description, Quantity,Price from shoppingcart where Pid=%s;"
    cur.execute(sql,(Pid,))
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
    sql="update shoppingcart set Name=%s, Description=%s, Quantity=%s, Price=%s where Pid=%s and Pid IN (select Pid from shoppingcart);"
    cur.execute(sql,(name,des,number,price,Pid))
    conn.commit()
    return True

def addgoodsN(Pid,number):
    sql="update shoppingcart set Quantity=Quantity+%s where Pid=%s and Pid IN (select Pid from shoppingcart);"
    cur.execute(sql,(number,Pid))
    conn.commit()
    return True

