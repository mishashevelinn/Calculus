from sympy import *


def lim(expression, a, x):
    print("lim[ {} ]-->{} \nx-->{}".format(expression, limit(expression, x, a), a))


def delambert(expression, a, x):
    nominator = expression.subs(x, x + 1)
    denominator = expression
    res = limit(nominator / denominator, x, a)
    if res < 1:
        print("Converges by D'elambert")
    elif res == 1:
        print("D'elambert test failed... try another one")
    else:
        print("The series is not fundamental by D'elambert test")


def cauchy(expression, a, x):
    res = limit((expression ** (1 / x)), a, x)
    print(res, type(res))
    if res == 1:
        print("Cauchy test failed... try another one")
    elif (res > 1) or (res == oo) or (res == -oo):
        print("The series is not fundamental by Cauchy test")
    else:
        print("Converges by Cauchy test")


def asymptote(expression, x):
    a = limit((expression / x), x, oo)
    if (a != oo) and (a != -oo):
        b = limit((expression - (a * x)), x, oo)
    else:
        print("angle of asymptote is infinity => no angled asymptote\n")
        return
    if (b != oo) and (b != -oo):
        if a != 0:
            print("y = {}x + {}".format(a, b))
        else:
            print("y = {}\nHorizontal asymptote is a private case of angled(slope = 0)\n".format(b))
    else:
        print("asymptote and y axe intersection is infinity => no angled asymptote\n")


def screen():
    print("Welcome to PyHedva!\nMenu\nTip of the day: in Python infinity defined by oo - double 'o' chars")
    print("1 - Find a limit of sequence\n2 - Use D'elambert test\n3 - Use Cauchy test\n4 - Find angled asymptote")


def initialize():
    button = int(input())
    x = symbols('x')
    func = eval(input("enter the function: "))
    if button != 4:
        a = input("x tends to: ")
    if button == 1:
        lim(func, a, x)
    if button == 2:
        delambert(func, a, x)
    if button == 3:
        cauchy(func, a, x)
    if button == 4:
        asymptote(func, x)


def main():
    screen()
    initialize()
    print("To go back to main menu press 0\nTo exit press any key")
    c = int(input("\n"))
    while c == 0:
        screen()
        initialize()
        print("To go back to main menu press 0\nTo exit press any key")
        c = int(input())

main()
