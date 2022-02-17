def num_translate(eng):
    num = {'zero': 'ноль', 'one': 'один', 'two': 'два',
           'three': 'три', 'four': 'четыри', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
           'nine': 'девять', 'ten': 'десять', }
    return num.get(eng)


print(num_translate(input('Enter a number up to ten: ')))
