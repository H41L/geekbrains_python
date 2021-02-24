durations_list = [0, 53, 153, 4153, 400153]

for duration in durations_list:
    seconds = duration % 60
    minutes = duration // 60 % 60
    hours = duration // 3600 % 24
    days = duration // 86400
    print("duration =", duration)
    if days == 0 and hours == 0 and minutes == 0:
        print(seconds, "сек")
    elif days == 0 and hours == 0:
        print(minutes, "мин", seconds, "сек")
    elif days == 0:
        print(hours, "час", minutes, "мин", seconds, "сек")
    else:
        print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
