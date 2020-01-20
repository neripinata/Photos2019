import re
import random

dataset = "qualification_round_2019.in/a_example.txt"
retry = True

f = open(dataset, "r")
#print(f.read())

text = f.read()

output = []

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

def replace_value_with_definition(key_to_find, definition):
    for key in categories.keys():
        if key == key_to_find:
            categories[key] = definition



for i in range(len(categories)):
    for i in range(len(categories) * 10):
        number = random.randrange(len(categories))
        types = (rx.split(text))
        photo_one = (simple_space.split(categories[number]))
        for i in range(len(categories)):
            number_dos = random.randrange(len(categories))
            while number_dos == number:
                number_dos = random.randrange(len(categories))
            types = (rx.split(text))
            photo_two = (simple_space.split(categories[number_dos]))
        
    #print(photo_one)
    #print(photo_two)

    similarities =  set(photo_one[2:]) & set(photo_two[2:])

    if not similarities:
        pass
    else:
        output.append(number)
        output.append(number_dos)
        replace_value_with_definition(number, 'Used')
        replace_value_with_definition(number_dos, 'Used')
        retry = False


print(output)

#print(types)