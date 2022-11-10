#!C:\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi

import shopcart as sp
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>修改商品結果</title>
</head>
<body>
""")
form = cgi.FieldStorage()
Pid = form.getvalue('Pid')
name = form.getvalue('name')
des = form.getvalue('des')
number = form.getvalue('number')
price = form.getvalue('price')
if Pid == None or name == None or price == None:
    print("錯誤的輸入")
elif int(number) < 0:
    print("數量不可為負")
elif int(price) < 0:
    print("價格不可為負")
else:
    if sp.check(Pid):
        if sp.changegoods(Pid,name,des,number,price):
            print("修改商品成功!")
        else:
            print("修改商品失敗!")
    else:
        print("沒有這個商品")
print("<br><a href='goodslist.py'>回管理端</a>")
print("</body></html>")