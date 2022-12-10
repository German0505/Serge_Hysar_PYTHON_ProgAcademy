# 1. Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. Наприклад, користувач вводить рядок 0,5,10,15,20,25
#

variable_1, variable_2 = 2, 3

def sequence(a):
    for i in range(len(a)):
        if int(str(a[1])) - int(str(a[0])) == variable_1 and int(str(a[2])) - int(str(a[1])) == variable_1:
            res= int(str(a[-1])) + variable_1

        if int(str(a[2])) - int(str(a[1])) == variable_2:
            res = int(str(a[-1])) + variable_2

        if int(str(a[1])) == (i + 1) ** variable_2:
            res=  round(((int(str(a[-1])) ** (1. / 3.) + 1) ** variable_2))


        if int(str(a[1])) == (i + 1) ** variable_1:
            res=  round((int(str(a[-1])) ** 0.5 + 1) ** variable_1)


        if (int(str(a[1]))) == variable_2 ** i:
            res=  int(str(a[-1])) * variable_2


        if (int(str(a[2]))) == variable_1 ** i:
            res=  int(str(a[-1])) * variable_1
    return res


a = list(input().split(","))

print(sequence(a))
#
# 2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел. Виведіть значення цього паліндрому і те, vyj;tyyzv яких чисел він є.

def palindrome():
    list,list_2 = [],[]
    for i in range(100, 1000):
        for j in range(100, 1000):
            product=i*j
            if str(product)[:]==str(product)[::-1] and len(str(product))==6:
                list.append(int(product))
                if i * j == max(list):
                    multiplier_1,multiplier_2=i,j
                    list_2.append(max(list))
    return f'Значення паліндрому - {max(list_2)}, множники числа: {multiplier_1} та {multiplier_2}'



