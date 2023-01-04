import random

n = int(input('Введите размер списка '))
my_list = []
for i in range(0, n):
    my_list.append(random.randint(0, 5))
print(my_list)
y = 0
for i in my_list:
    for j in my_list[y + 1:]:
        if i == j:
            my_list.remove(j)
    y += 1
print(my_list)

