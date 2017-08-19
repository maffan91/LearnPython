months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# slicing example
first_half_year = months[0:6]
second_half_year = months[6:12]

print("First Half:")
print(first_half_year)
print("Second Half:")
print(second_half_year)
first_quarter = months[:3]

print("Q1")
print(first_quarter)
last_quarter = months[9:]

print("Q4")
print(last_quarter)

print("Negative Slicing:")
print(months[-4:-1])