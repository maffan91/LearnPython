# name = 'Affan'
# print('New Python Calling my name: ' + name)

age = 1
minimumAgeLimitForBoys = 18
minimumAgeLimitForGirls = 16
if age > minimumAgeLimitForBoys:
    print('You are in...')
else:
    print('Sorry this time, but we\'ll be happy to see you after ' + str (minimumAgeLimitForBoys - age) + ' years')

if True == False:
    print('True')
elif False == True:
    print('False')
else:
    print('Hi')