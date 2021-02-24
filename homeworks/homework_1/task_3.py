percents = int(input())
last_num = percents % 10
last_two_nums = percents % 100

if last_num == 1 and last_two_nums != 11:
    print(percents, "процент")
elif (last_num == 2 or last_num == 3 or last_num == 4) and (last_two_nums != 12 and last_two_nums != 13 and
                                                            last_two_nums != 14):
    print(percents, "процента")
else:
    print(percents, "процентов")
