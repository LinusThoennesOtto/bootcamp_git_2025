def main():
    x = 2.0
    y = 4.0

    print(f"{x} + {y} = {add(x, y)}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

def multi(x, y):
    return x * y


if __name__ == '__main__':
    print("Hi, ich bin dein persönlicher Taschenrechner! Let's start:")
    main()
