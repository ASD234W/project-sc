#!C:\Python\Python310\python.exe
#-*- coding: utf-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi

import shopcart as sp
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>確認購物車內容</title>
</head>
<body>
<h2>結帳前確認</h2>
""")
msgList=sp.listcart()
if msgList:
    for (Pid,Name,Description,Quantity,Price) in msgList:
        print(f"<p>商品編號{Pid}: 商品名稱:{Name} 商品簡介:{Description} 數量:{Quantity} 商品價格:{Price}</p>")
else:
    print("購物車是空的")
print("""
<hr>
<a href='SFinish.py'> 結帳</a>
 <hr>
 <br><a href='Customer.py'>回客戶端</a>
 </body></html>
 """)