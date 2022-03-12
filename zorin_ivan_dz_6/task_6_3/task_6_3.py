import json
import sys

result_dict = {}
with open('users.csv', 'r', encoding='utf-8') as f_1, \
        open('hobby.csv', 'r', encoding='utf-8') as f_2:
    users = (el for el in f_1.read().splitlines())
    hobbies_data = (el for el in f_2.read().splitlines())
    for hobbies, user in zip(hobbies_data, users):
        result_dict[user.strip()] = hobbies.strip()
    for _ in hobbies_data:
        sys.exit(1)
    for user in users:
        result_dict[user.strip()] = None
print(result_dict)
with open('result.json', 'w', encoding='utf-8') as result_file:
    json.dump(result_dict, result_file, ensure_ascii=False)
