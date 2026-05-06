# This is a simple Python script that demonstrates the use of if-else statements and functions.

# Control flow with if-else statements and loops
cities = ['San Francisco', 'Los Angeles', 'New York', 'Atlanta']
for city in cities:
    if city == 'Los Angeles':
        pass
    else:
        print(city)

for city in cities:
    if city == 'Los Angeles':
        continue
    else:
        print(city)

# Looping through numbers and checking divisibility
for x in range(1, 10):
    if x%2 == 0:
        print('{} is divisible by 2'.format(x))
    else:
        print('{} is not divisible by 2'.format(x))


# This is a function that greets a person by name
def greet(name):
    x = 'Hello ' + name
    return x

print(greet('Habtamu'))