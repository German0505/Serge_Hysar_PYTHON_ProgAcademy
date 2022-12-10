# 1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
# Наприклад, 1 - "Monday".

days_of_the_week = {
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday",
    7:"Saturday"
}
print(days_of_the_week.get(int(input()), "wrong key"))

# 2. Опишіть кота (домашня тварина) на основі словника.

cat = {
    "nickname": "Phyton",
    "weight": "2.267 kg",
    "date of birth": "2021-08-17",
    "breed": "Persian",
    "color": "White",
    "social insurance number": "637316241",
    "contact": "Gagarina Street 5/2, Brovary 07400 Ukraine"}
print(cat)

# 3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику, скільки разів яка літера зустрічається в цьому рядку.
# Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.


text = input()
dict_ = {}
for i in text:
    if dict_.get(i):
        dict_[i] += 1
    else:
        dict_[i] = 1
print(dict_)


# 4. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери, які є одночасно і в першому,
# і в другому рядку. Наприклад, для рядків «Hello» та «World» на екрані мають бути літери «l» та «o».

print(set(input()) & set(input()))

# 5. Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.

import random

list_1,list_2 = [i for i in range(random.randint(1,100)) if not i % 3], [i for i in range(random.randint(1,100)) if not i % 5]

print(list_1,list_2, sep='\n')

# 6. Створіть список із числами, які є в обох списках.

print(set(list(input())) & set(list(input())))