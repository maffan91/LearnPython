# practicing loops

hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]
elements = []
# for loop practice
for i in hairs:
    elements.append(i)

for i in eyes:
    elements.append(i)
for i in weights:
    elements.append(i)

for i in elements:
    print(i)
print(elements.__len__())


# while loop practice
num = 1024

while num % 2 == 0 and num != 0:
    print(num)
    num /= 2