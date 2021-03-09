def num_translate_adv(num):
    if num.istitle():
        print(translate_num_dict.get(num.lower()).capitalize())
    else:
        print(translate_num_dict.get(num))


translate_num_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

num_translate_adv('one')
num_translate_adv('One')
num_translate_adv('Eight')
num_translate_adv('ten')
