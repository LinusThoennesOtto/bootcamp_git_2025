last = None

def main(last=None):
    x = input("Zahl 1: " if last == None else f"Zahl 1 (leerlassen um {last} zu übernehmen): ")
    if x == "" and last != None:
        x = last
    else:
        x = float(x)
    y = float(input("Zahl 2: "))

    match(input("Rechnung: ").lower()):
        case "+" | "plus" | "addieren" | "addition":
            print(f"{x} + {y} = {add(x, y)}")
            return add(x, y)
        case "-" | "minus" | "subtrieren" | "subtraktion":
            print(f"{x} - {y} = {sub(x, y)}")
            return sub(x, y)
        case "*" | "mal" | "multiplizieren" | "multiplikation":
            print(f"{x} * {y} = {multi(x, y)}")
            return multi(x, y)
        case "/" | "geteilt" | "durch" | "dividieren" | "division":
            print(f"{x} / {y} = {geteilt(x, y)}")
            return geteilt(x, y)
        case _:
            print("Kein valider Operator.")


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
        last = main(last)



def ask_input():
    x = input("x")
    y = input("y")
    operator = input("+/-")
