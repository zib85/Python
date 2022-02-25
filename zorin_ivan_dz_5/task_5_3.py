TUTORS = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена', 'Ольга', 'Илья']
KLASSES = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def my_gen():
    _tutors = (el for el in TUTORS)
    _klasses = (el for el in KLASSES)
    for _school in zip(_klasses, _tutors):
        yield _school[::-1]
    for rest in _tutors:
        yield rest, None


my_gener = my_gen()
for item in my_gener:
    print(item)
