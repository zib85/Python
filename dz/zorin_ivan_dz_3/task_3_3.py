def thesaurus(names):
    names_dict = {}
    for name in names:
        first_spelling = name[0]
        if names_dict.get(first_spelling):
            names_dict[first_spelling].append(name)
        else:
            names_dict.setdefault(first_spelling, [name])
    return names_dict


users = ("Контсантин", "Борис", "Николай", "Богдан", "Антон",
         "Никита", "Андней", "Ольга", "Мария", "Михаил")
users_new = sorted(users)
name_list = thesaurus(users_new)
print(name_list)
