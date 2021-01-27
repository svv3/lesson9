#5. Создать словарь, где ключ - значение списка users, значение - значение списка marks
#Использовать встроенную в python функцию zip

users = ["Ann", "Jane", "Bob", "Bill", "John"]
marks = [5, 4, 3, 4, 5]
a=zip(users, marks)
print(dict(a))
