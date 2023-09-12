'''print("*" * 10, "Задание №1. из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343} ", "*" * 10)

list1=[1,2,3,4,5,6,7]
list2 = [i if i<0 else i**3 for i in list1 if i%2!=0]
list3 = [i if i>0 else i**3 for i in list1 if i%2!=0]
print(dict(zip(list3, list2)))'''

'''print("*" * 10, "Задание №2. из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6} ", "*" * 10)

list=[1,2,3,4,4,5,6,6,6,7,7]
data = {i for i in list if i%2==0}
print(set(data))'''

print("*" * 10, "Задание №3. получить список [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] без исходногo", "*" * 10)

data = [i for i in range(0, 100) if i % 10 == 0]
print(data)