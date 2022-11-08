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
<title>修改商品項目</title>
</head>
<body>
<h2>原始資料</h2>
""")
form = cgi.FieldStorage()
Pid=form.getvalue('id')
msgList=sp.showgood(Pid)
for (Pid,Name,Description,Quantity,Price) in msgList:
	print(f"<p>商品編號{Pid}: 商品名稱:{Name} 商品簡介:{Description} 庫存:{Quantity} 商品價格:{Price}</p>")
print("""
<div >
<fieldset>
<legend>商品修改表單</legend>
<form method="post" action="changegoods.py">
輸入ID<input type="text" name='Pid'><br>
輸入名稱<input type="text" name='name'><br>
輸入簡介<input type="text" name='des'><br>
輸入數量<input type="number" name='number'><br>
輸入價錢<input type="number" name='price'><br>
<input type="submit">
</form>
</fieldset>
</div>
<br><a href='goodslist.py'>回管理端</a>
</body>
</html>
""")
