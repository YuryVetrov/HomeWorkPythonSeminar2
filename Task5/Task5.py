# Реализуйте алгоритм перемешивания списка.
import random
n = int(input('Введите число N = '))
spam = list(range(1, n+1))
print("Вы только что создали свой список", spam)
random.shuffle(spam)
print("Вот так выглядет Ваш развёрнутый список", spam)