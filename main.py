def main():
    x = float(input("Zahl 1: "))
    y = float(input("Zahl 2: "))

    match(input("Rechnung: ").lower()):
        case "+" | "plus" | "addieren" | "addition":
            print(f"{x} + {y} = {add(x, y)}")
        case "-" | "minus" | "subtrieren" | "subtraktion":
            print(f"{x} - {y} = {sub(x, y)}")
        case "*" | "mal" | "multiplizieren" | "multiplikation":
            print(f"{x} * {y} = {multi(x, y)}")
        case "/" | "geteilt" | "durch" | "dividieren" | "division":
            print(f"{x} / {y} = {geteilt(x, y)}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def geteilt(x, y):
    return x / y

if __name__ == '__main__':
    print("Hello User!")
    while True:
        main()


def ask_input():
    x = input("x")
    y = input("y")
    operator = input("+/-")
