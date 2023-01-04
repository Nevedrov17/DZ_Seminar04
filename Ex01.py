from math import pi

def t_pi (d):
    count = 0
    while d != 1:
        d *= 10
        count += 1
    print(round(pi, count))
d = float(input('Введите точность числа "pi" '))
t_pi(d)
