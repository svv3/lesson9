#4. Создать список, содержащий общие для двух данных списков числа

list_1 = [1, 2, 3, 4, 7, 15, 45]
list_2 = [2, 4, 6, 8, 15, 45, 10]
list_rep = []
a=[list_rep.append(i) for i in list_2 if i in list_1]
print(list_rep)
