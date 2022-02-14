employees_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАЯ', 'директор аэлита']
for item in employees_list:
    name = item.split()[-1].title()
    print('Привет,', name+'!')
