price_list = [98.5, 45, 37.5, 78, 23, 88.02, 73, 44, 54.2, 70.99,
              29.09, 55.34, 22.1, 99.99, 10.25]
new_price = []
for price in price_list:
    rubles = int(price)
    kk = round((price - rubles) * 100)
    new_price.append(f"{rubles} руб {kk:02d} коп")
print(", ".join(new_price))

id_1 = id(price_list)
price_list.sort()
print(price_list)
print(id_1)               # сравнение значений id
print(id(price_list))

new_list = sorted(price_list, reverse=True)
print(new_list)
print(id(new_list))
print(sorted(new_list[:5]))
