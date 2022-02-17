def num_translate(eng):
    num = {'zero': 'ноль', 'one': 'один', 'two': 'два',
           'three': 'три', 'four': 'четыри', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
           'nine': 'девять', 'ten': 'десять', }
    if result := num.get(eng.lower()):
        return result if eng[0].islower() else result.title()


print(num_translate(input('Enter a number up to ten: ')))
