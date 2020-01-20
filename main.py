import re
import random

dataset = "qualification_round_2019.in/a_example.txt"


f = open(dataset, "r")
#print(f.read())

text = f.read()


rx = re.compile(r'\s{2,}|\n+')
simple_space = re.compile(r'\s{1,}|\n+')
types = (rx.split(text))

categories = {}

t = 0

for i in types[1:len(types)-1]:
    categories[t] = i
    t += 1


print(categories)

print(len(categories))

for i in range(len(categories)):
    number = random.randrange(len(categories))
    types = (rx.split(text))
    etiquetas = (simple_space.split(categories[number]))
    print(etiquetas)

#print(types)