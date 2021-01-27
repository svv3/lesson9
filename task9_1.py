#1. Написать программу, которая создает список, содержащий длину каждого слова, длиннее чем переменная n
#использовать list comprehension

n=int(input())
sentence = "Python is a programming language that lets you work quickly and integrate systems more effectively."
a=[i for i in sentence.split() if n<len(i)]
print(a)
