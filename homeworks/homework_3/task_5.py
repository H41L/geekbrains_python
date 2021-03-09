import random


def get_jokes(n, repeat_words=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    if not repeat_words:
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
    for i in range(n):
        if repeat_words:
            jokes_list.append(' '.join([random.choice(nouns),
                                        random.choice(adverbs),
                                        random.choice(adjectives)]))
        else:
            if i == len(nouns) or i == len(adverbs) or i == len(adjectives):
                break
            jokes_list.append(' '.join([nouns[i], adverbs[i], adjectives[i]]))
    print(jokes_list)


get_jokes(10)
get_jokes(10, False)
