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
<title>結帳</title>
</head>
<body>
""")
msglist=sp.SFinish()
if sp.SFinish():
    for (total) in msglist:
        if total != None:
            print(f"結帳成功，總共：{total}元")
        else:
            print("購物車是空的，無法結帳")
else:
    print("結帳失敗!")
print("<br><a href='Customer.py'>回客戶端</a>")
print("</body></html>")