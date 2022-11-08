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
<title>加入購物車</title>
</head>
<body>
""")
form = cgi.FieldStorage()
Pid=form.getvalue('id')
number=form.getvalue('number')
if Pid == None or number == None:
    print("輸入格式錯誤")
elif sp.addcart(Pid,number):
    print(f"編號{Pid}商品已加入購物車!")
else:
    print("加入購物車失敗!")
print("<br><a href='Customer.py'>回客戶端</a>")
print("</body></html>")