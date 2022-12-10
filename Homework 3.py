# 1. Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці. На одному поверсі - 4 квартири. '
# 'Напишіть програму, яка від користувача отримує номер квартири та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі.
# Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це.

flat_number=int(input("Please,enter the apartment number:"))
number_of_apartments=144

entrance= ((flat_number - 1) // 36) + 1
floor=(((flat_number - 1) % 36)//4) + 1
room_on_the_floor=((flat_number - 1)%4) + 1
res=(flat_number<=number_of_apartments) and ("Ґанок="+ str(entrance),"Поверх="+ str(floor), "Номер на поверсі="+str(room_on_the_floor))
print(res or "This is a fake flat")

# 2. Написати програму, яка буде повертати для заданого року кількість днів.
# Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400

Year = int(input())

if (Year % 4 == 0) and (Year % 100 != 0) or (Year % 400 == 0):
    print("Result: 366")
else:
    print("Result:365")

# 3. Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої.
# Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує такий трикутник.

A,B,C =float(input()),float(input()),float(input())

if A + B > C and A + C > B and B + C > A:
    print('This is a triangle')
else:
    print('This is not a triangle')
