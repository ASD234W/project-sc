#!C:\Python\Python310\python.exe
#-*- coding: utf-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi

import shopcart as sp
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>客戶端購物車</title>
</head>
<body>
<a href='addgoodsform.html'> 新增商品 </a><hr>
<form method="post" action="delgoods.py">
輸入要刪除的ID: <input type='text' name='i'><input type='submit'>
</form> <br>
<a href='changeGform.html'> 修改商品庫存 </a><hr>
<hr>
""")
msgList=sp.goodslist()
for (Pid,Name,Description,Quantity,Price) in msgList:
	print(f"<p>商品編號{Pid}: 商品名稱:{Name} 商品簡介:{Description} 庫存:{Quantity} 商品價格:{Price}</p>")

print("</body></html>")
