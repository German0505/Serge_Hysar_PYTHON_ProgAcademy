# 1. Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
# Примітка: щасливим квитком називається число, у якому, при парній кількості цифр,
# сума цифр його лівої половини дорівнює сумі цифр його правої половини.
# Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.


ticket=list(input())
left_half,right_half=int(ticket[0])+int(ticket[1]),int(ticket[2])+int(ticket[3])
res=(left_half==right_half) and "Lucky ticket"
print(res or "Unlucky ticket")

# 2. З клавіатури вводиться число (шестизначне). Перевірити, чи воно є паліндромом.
# Примітка: Паліндром називається число, слово або текст, які однаково читаються зліва направо і справа наліво.
# Наприклад, це числа 143341, 5555, 7117 і т.д.

ticket=list(input())
res=(ticket[:]==ticket[::-1]) and "A palindrome number"
print(res or "Non-palindromic number")

# 3. Дано коло з центром на початку координат та радіусом 4. Користувач вводить з клавіатури координати точки x та y.
# Написати програму, яка визначить, лежить ця точка всередині кола чи ні.

RADIUS=4
x,y=map(float,input("Please, enter the coordinates of a point:").split())

res=((x**2+y**2)<=RADIUS**2) and "Point inside a circle"
print(res or "Point outside the circle")





