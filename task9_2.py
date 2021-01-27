#2. C помощью list comprehension сгенерировать новый список только с позитивными целыми числами

numbers = [2, -2.4, 3.3, -1, 7, 12, -11, 9.5]
a=[i for i in numbers if i>=0 and type(i)==int or i%2==0]
print(a)
