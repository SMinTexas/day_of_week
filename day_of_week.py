#Given the following code that prompts the user for a day number
#(the int function converts a numeric string to a number):
#   day = int(input('Day (0-6)? '))

#The user will enter a number between 0 and 6 inclusive.  Given
#this number, print a day of the week. 0 for Sunday, 1 for Monday,
#2 for Tuesday, and so on.

day = int(input('Day (0-6)? '))

if day == 0:
    print('Sunday')
elif day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
else:
    print('Saturday')