if __name__ == '__main__':
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for price in f:
            print(price.strip())
