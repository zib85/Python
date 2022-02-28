import requests


def corrency_rates(val):
    website = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = website.content.decode(encoding=website.encoding)
    result = None
    if val not in content:
        for el in content.split('<NumCode>')[1:]:
            print((el.split('</NumCode>')[0]), '-', (el.split('<Name>')[1].split('</Name>')[0]))
        return result

    else:
        for el in content.split(f'{val}')[1:]:
            for el_1 in el.split('</Value>')[:1]:
                result = round(float(el_1.split('<Value>')[1].replace(',', '.')), 2)
                return f'Курс валюты: {result} руб.'


if __name__ == '__main__':
    code_val = input('Введите код валюты: ')
    print(corrency_rates(code_val))