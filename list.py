import os

list1 = [4, 9, 3, 15, 1]

list2 = list1

for i in list1:
    print(i)


print(list2)


print(list1.sort())
print(list1.sort())



list3 = [4, 9, 3, 15, 1]
list4 = sorted(list3)

print("list1:", list3)
print("list2:", list4)


class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3))


print(Calculator().add(9, 1))
