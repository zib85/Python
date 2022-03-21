import re


def email_pars(email_address):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = pattern.match(email_address)
    if not result:
        raise ValueError(f'Электронный адрес невалиден: {email_address}')
    return result.groupdict()


print(email_pars('someone@geekbrains.ru'))
print(email_pars('someone@geekbrainru'))
