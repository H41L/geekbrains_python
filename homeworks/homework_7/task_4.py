import os

if __name__ == '__main__':
    folder = 'some_data'
    result = {
        0: 0,
        10: 0,
        100: 0,
        1000: 0,
        10000: 0,
        100000: 0,
        1000000: 0,
    }

    for root, dirs, files in os.walk(folder):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            for key in result:
                index = key
                next_key = key * 10
                if next_key == 0:
                    next_key = 10
                if index < size <= next_key:
                    result[next_key] += 1
    print(result)
