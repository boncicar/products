# 輸入商品名稱及價格

products = []   # 建立大清單products
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')  # 此行寫在if外以及if之後是避免輸入q要跳出程式時會出現請輸入商品價格
	products.append([name, price])   # 直接把小清單x裝入products清單內，程式更簡潔
print(products)

# produts[1][0]:1表示products大清單內的第1位置，0表示在products第1位置內的x清單的第0位置