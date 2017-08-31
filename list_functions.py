sample_list = [
    'Atlas',
    'Bible',
    'Catastrophic',
    'Dangerous'
]
# joining the letters of each list item together
print(''.join(sample_list))

# making list out of strings
string_eg = 'PAKISTAN'
str_to_list = list(string_eg)
print(str_to_list)

str_to_list[3:] = list('PATTAN')
print(str_to_list)

str_to_list[:2] = list('PAAAAK')
print(str_to_list)