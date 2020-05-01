# 輸入商品名稱及價格

products = []   # 建立大清單products
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')  # 此行寫在if外以及if之後是避免輸入q要跳出程式時會出現請輸入商品價格
	x = []     # 建立第二個清單x(二維清單)，目的要把name跟price裝進x，即為x = [name, price]
	x.append(name)   # 把name裝進x清單中的第0位置
	x.append(price)  # 把price裝進x清單中的第1位置
	products.append(x)  # 把x清單裝入products清單內
print(products)

# produts[1][0]:1表示products大清單內的第1位置，0表示在products第1位置內的x清單的第0位置