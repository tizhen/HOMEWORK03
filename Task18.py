# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:

# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input("Размер массива: ")) 
print("Элементы массива:")
A = sorted(list(map(int, input().split())))
x = int(input("Число x: ")) 

res = []

for num, i in enumerate(A):
    if i >= x:
        if x - A[num - 1] > A[num] - x:
            res.append(A[num])
        else:
            res.append(A[num - 1])
            
if res:
    print(res[0])
else:
    print(max(A))


# import sys
# A=list(map(int,input().split()))
# X=int(input())
# c=[]
# for i in A:
#     c.append(abs(X-i))
# d=c.index(min(c))
# print(A[d])