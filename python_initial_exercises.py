print "Hello World"
print "This is not my first python script :D"

print "Summary till ex.10"

# this is how we comment the code in python

name = "Affan"

# this is how to print variables in python
print "My name is %s" % name

# some of the decisions making
print 5 < 7
print 5 <= 5

age = 17

if age < 18:
    print "your too young to join the party"

# new chap: numbers and maths

cars = 45
spaceInCars = 5.0
passengers = 76
drivers = 34

if drivers < cars:
    print "Not all cars will be driven"

# seating arrangements will be like

carsDriven = drivers
passengersCanBeTaken = carsDriven*spaceInCars - drivers
print passengersCanBeTaken
if passengersCanBeTaken > (passengers+drivers):
    print "All passengers can travel"
else:
    print "Sorry insufficient cars"
