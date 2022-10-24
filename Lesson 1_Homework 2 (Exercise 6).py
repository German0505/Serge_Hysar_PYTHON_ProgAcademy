


# 6.Write a program that calculates and displays the area of a triangle if its sides are known

# Згідно умов невідомо, чи трикутний рівносторонній, прямокутний, ін. Тому, площу можливо вирахувати згідно формули Герона
# p - полумериметр трикутника p=(a+b+c)/2
# Формула Герона:   s=(p(p-a)(p-b)(p-c))*0.5

side1,side2,side3=5,6,7

p=(side1+side2+side3)/2
area=(p*(p-side1)*(p-side2)*(p-side3))**0.5
print(area)