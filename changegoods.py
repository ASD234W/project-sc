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

if sp.changegoods(Pid,name,des,number,price):
    print("修改商品成功!")
else:
    print("修改商品失敗!")
print("<br><a href='goodslist.py'>回管理端</a>")
print("</body></html>")