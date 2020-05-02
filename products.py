# 輸入商品名稱及價格

products = []   # 建立大清單products
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')  # 此行寫在if外以及if之後是避免輸入q要跳出程式時會出現請輸入商品價格
	products.append([name, price])   # 直接把小清單x裝入products清單內，程式更簡潔
print(products)
for x in products:  # 以x來讀取products清單中的每一筆資料
	print(x[0], '的價格是', x[1], '元')        # 印出products清單中的每一筆資料: 商品名稱 + 的價格是+ 價格 + 元
