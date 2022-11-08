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
<title>刪除商品</title>
</head>
<body>
""")
form = cgi.FieldStorage()
Pid=form.getvalue('id')
if Pid == None:
    print("發生錯誤")
elif sp.delgoods(Pid):
    print(f"編號{Pid}商品已刪除!")
else:
    print("刪除商品失敗!")
print("<br><a href='goodslist.py'>回管理端</a>")
print("</body></html>")
