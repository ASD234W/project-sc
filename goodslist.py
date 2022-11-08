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
<title>管理端</title>
</head>
<body>
特殊動作 <a href='Customer.py'> 客戶端 </a><hr>
<a href='addgoodsform.html'> 新增商品 </a> 
<form method="post" action="delgoods.py">
輸入要刪除的ID: <input type='text' name='id'><input type='submit'>
</form>
<form method="post" action="changeGform.py">
輸入要修改的ID: <input type='text' name='id'><input type='submit'>
</form>
<form method="post" action="addgoodsN.py">
輸入要入庫的商品ID: <input type='text' name='id'> 數量: <input type='number' name='number'><input type='submit'>
</form>
<hr>
<h2>商品清單</h2>
""")
msgList=sp.goodslist()
for (Pid,Name,Description,Quantity,Price) in msgList:
	print(f"<p>商品編號{Pid}: 商品名稱:{Name} 商品簡介:{Description} 庫存:{Quantity} 商品價格:{Price}</p>")

print("</body></html>")
