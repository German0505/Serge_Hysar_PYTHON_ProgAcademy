# 1. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.

def concatenate(x, y, row):
    print(row + str(x + y))

concatenate(1, 2, "Sum of numbers = ")


# 2. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*». Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.


def rectangle (x,y):
    print ( y *'*')
    for i in range (1,x-1):
        print ('*', (y-2)*'','*')
    print (y*'*')
rectangle(4,5)


# 3. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел. Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».


def search_for_items (item, list_):
    # item = input()
    # list_ = list(input())

    for i in list_:
        if item == list_[i]:
            return i
    return -1
print(search_for_items(2,range(4)))



# 4. Напишіть функцію, яка поверне кількість слів у текстовому рядку.

def count_(a):
    print(len(a.split()))
count_('Напишіть функцію, яка поверне кількість слів у текстовому рядку')

# 5. Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents

def in_writing(a):

    left_side = a[0]
    right_side = a[1]

    number = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
              '9': 'nine', '10': 'ten',
              '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen',
              '17': 'seventeen', '18': 'eighteen',
              '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty',
              '70': 'seventy', '80': 'eighty', '90': 'ninety'}

    if len(left_side) == 6:

        if left_side[1] == '1' and left_side[4] == "1":
            res = (f'{number.get(left_side[0])} hundred {number.get(left_side[1] + left_side[2])}  '
                   f'thousand {number.get(left_side[3])} hundred {number.get(left_side[4] + left_side[5])} dollars')
        elif left_side[4] == '1':
            res = (f'{number.get(left_side[0])} hundred {number.get(left_side[1] + "0")} {number.get(left_side[2])}  '
                   f'thousand {number.get(left_side[3])} hundred {number.get(left_side[4] + left_side[5])} dollars')
        elif left_side[1] == '1':
            res = (f'{number.get(left_side[0])} hundred {number.get(left_side[1] + left_side[2])}   '
                   f'thousand {number.get(left_side[3])} hundred {number.get(left_side[4] + "0")} {number.get(left_side[5])} dollars')
        else:
            res = (f'{number.get(left_side[0])} hundred {number.get(left_side[1] + "0")} {number.get(left_side[2])} '
                   f'thousand {number.get(left_side[3])} hundred {number.get(left_side[4] + "0")} {number.get(left_side[5])} dollars')

    if len(left_side) == 5:
        if left_side[0] == '1' and left_side[3] == "1":
            res = (f'{number.get(left_side[0] + left_side[1])} thousand {number.get(left_side[2])}  '
                   f'hundred {number.get(left_side[3] + left_side[4])} dollars')
        elif left_side[0] == '1':
            res = (f'{number.get(left_side[0] + left_side[1])} thousand {number.get(left_side[2])}  '
                   f'hundred {number.get(left_side[3] + "0")} {number.get(left_side[4])} dollars')
        elif left_side[3] == '1':
            res = (f'{number.get(left_side[0] + "0")} thousand {number.get(left_side[2])}  '
                   f'hundred {number.get(left_side[3] + left_side[4])} dollars')
        else:
            res = (f'{number.get(left_side[0] + "0")} {number.get(left_side[1])}thousand   {number.get(left_side[2])}  '
                   f'hundred {number.get(left_side[3] + "0")} {number.get(left_side[4])} dollars')

    if len(left_side) == 4:
        if left_side[2] == '1':
            res = (f'{number.get(left_side[0])} thousand {number.get(left_side[1])}  '
                   f'hundred {number.get(left_side[3] + left_side[4])} dollars')
        else:
            res = (f'{number.get(left_side[0])} thousand {number.get(left_side[1])}  '
                   f'hundred {number.get(left_side[2] + "0")} {number.get(left_side[3])} dollars')

    if len(left_side) == 3:
        if left_side[1] == '1':
            res = (f'{number.get(left_side[0])} hundred {number.get(left_side[1] + left_side[2])} dollars')
        else:
            res = (
                f'{number.get(left_side[0])} hundred {number.get(left_side[1] + "0")} {number.get(left_side[2])} dollars')

    if len(left_side) == 2:
        if left_side[0] == '1':
            res = (f'{number.get(left_side[0] + left_side[1])} dollars')
        else:
            res = (f'{number.get(left_side[0] + "0")} {number.get(left_side[1])} dollars')

    if len(left_side) == 1:
        res = (f'{number.get(left_side[0])} dollars')

    if len(right_side) == 2:
        if right_side[0] == '1':
            res_1 = (f'{number.get(right_side[0] + right_side[1])} cent')
        else:
            res_1 = (f'{number.get(right_side[0] + "0")} {number.get(right_side[1])} cent')

        return f'{res}  {res_1}'
a = input().split(",")
print(in_writing(a))


# 6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22
roman_n = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def roman_numerals (num):
    rom = ''
    while num > 0:
        for i, r in roman_n:
            while num >= i:
                rom += r
                num -= i
    return rom

print(roman_numerals(15))
