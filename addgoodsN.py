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
<title>修改商品庫存</title>
</head>
<body>
""")
form = cgi.FieldStorage()
Pid=form.getvalue('id')
number=form.getvalue('number')
if Pid is None or number is None:
    print("錯誤的輸入")
else:
    if sp.check(Pid):
        if sp.addgoodsN(Pid,number):
            print(f"編號{Pid}商品庫存已修改!")
        else:
            print("修改庫存失敗!")
    else:
        print("沒有這個商品")
print("<br><a href='goodslist.py'>回管理端</a>")
print("</body></html>")