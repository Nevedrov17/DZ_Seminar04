def prost_num(num):
    i = 2
    lst = []
    old = num
    while i <= num:
        if num % i == 0:
            lst.append(i)
            num //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {old} приведены в списке: {lst}")
num = int(input("Введите число: "))
prost_num(num)