# Get user age
age = int(input('Enter your age: '))

# Determine and display age classifier
if age <= 1:
    print('You are an infant.')
elif age > 1 and age < 13:
    print('You are a child.')
elif age >= 13 and age < 20:
    print('You are a teenager.')
else:
    print('You are an adult.')
