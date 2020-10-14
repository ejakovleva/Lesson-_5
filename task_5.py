import random

numbers_list = []
numbers_quantity = 10
for _ in range(numbers_quantity):
    i = random.randrange(7, 500)
    numbers_list.append(f'{i} ')

with open("text_5.txt", 'w', encoding='utf-8') as num_file:
    print("".join(numbers_list), file=num_file)


with open("text_5.txt", 'r', encoding="utf-8") as file_num:
    print(sum([float(i) for i in file_num.read().split()]))
