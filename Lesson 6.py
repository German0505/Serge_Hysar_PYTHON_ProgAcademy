# 1.Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту

print(input().count('b'))

# 2. Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки введеного ім'я на валідність
# (мається на увазі, що, наприклад, в імені людини не може бути цифр, воно повинно починатися з великої літери, за якою повинні йти маленькі).

name=input()
if name.isalpha() and name==name.capitalize():
    print("It's a real name")
else: print("It's a unreal name")

# 3.Напишіть програму, яка обчислить суму всіх кодів символів рядка.

row= input()
sum_=0
for i in row:
    i=ord(i)
    sum_+=i
print(sum_)

# 4. Виведіть на екран 10 рядків із значенням числа Pi. У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.

import math
a = math.pi
n = 2
while n < 12:
    print(a.__round__(n))
    n += 1

# 5. Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.

string = input().split()
largest_word = string[0]
for word in string:
    if len(word) > len(largest_word):
        largest_word = word
print(largest_word)

# Додаткові задачі до домашнього завдання:
# 1. Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери).
# Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту. Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"

same_words = input()
translation =[]
for i in range(len(same_words)):
    if same_words[i] not in translation:
        translation.append(same_words[i])

print("".join(translation))