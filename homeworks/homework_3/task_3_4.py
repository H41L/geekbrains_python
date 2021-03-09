def thesaurus_adv(*args):
    args_list = list(args)
    result_dict = {}
    for item in args_list:
        temp_dict = {}
        split = str(item).split(" ")
        # Первый буквы имени и фамилии (ключи)
        name_letter = split[0][:1]
        surname_letter = split[1][:1]
        # Если ключа по первой букве фамилии нет, тогда добавляем его со значением в виде словаря:
        # <первая буква фамилии>:<<первая буква имени>:<[имя фамилия]>>
        if not result_dict.get(surname_letter):
            temp_dict[name_letter] = [item]
            result_dict[surname_letter] = temp_dict
        # Если ключа по первой букве имени нет в значениях по ключу фамилии, тогда добавляем его путем
        # обновления словаря (update)
        elif not result_dict.get(surname_letter).get(name_letter):
            temp_dict[name_letter] = [item]
            result_dict[surname_letter].update(temp_dict)
        # Иначе просто добавляем элемент в список по ключу
        else:
            result_dict.get(surname_letter)[name_letter].append(item)
    print(result_dict)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Анна Перова",
              "Алексей Березов", "Андрей Березов", "Сергей Березов")
