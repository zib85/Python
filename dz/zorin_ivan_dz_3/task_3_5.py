import random


def get_jokes(n, rep="no"):
    """ Generates <n> jokes from 3 lists
        param: - <n> number of jokes
        param: - <rep> enable or disable repetitions words in jokes (default _ "no")
        return: - <n> jokes of None
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if rep == "no":
        if n > len(nouns):
            return None
        else:
            noun = random.sample(nouns, n)
            adverb = random.sample(adverbs, n)
            adjective = random.sample(adjectives, n)
            result = [f"{noun[i]} {adverb[i]} {adjective[i]}" for i in range(len(noun))]
            return result

    else:
        noun = random.choices(nouns, k=n)
        adverb = random.choices(adverbs, k=n)
        adjective = random.choices(adjectives, k=n)
        result = [f"{noun[i]} {adverb[i]} {adjective[i]}" for i in range(len(noun))]
        return result


print(get_jokes(n=7))
print(get_jokes(n=5, rep="no"))
print(get_jokes(n=10, rep="yes"))
