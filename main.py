def main():
    x = float(input("Zahl 1: "))
    y = float(input("Zahl 2: "))

    print(f"{x} + {y} = {add(x, y)}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


if __name__ == '__main__':
    main()
