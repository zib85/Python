prognosis = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(*prognosis)  # исходные данные( возможно не использовать вывод).
new_prognosis = []
for el in prognosis:
    if el.isdigit():
        new_prognosis.extend('"'+el.zfill(2)+'"')
    elif el[1:].isdigit() and el[0] == "-" or el[0] == "+":
        new_prognosis.extend('"'+el.zfill(3)+'"')
    else:
        new_prognosis.append(el)
    new_prognosis.append(' ')
new_str = ''.join(new_prognosis)
print(new_str)
