# Input Specification
# The user will be prompted to enter two integers. First, the user will be prompted to enter the speed
# limit. Second, the user will be prompted to enter the recorded speed of the car.

# Output Specification
# If the driver is not speeding, the output should be:
# Congratulations, you are within the speed limit!
# If the driver is speeding, the output should be:
# You are speeding and your fine is $F .
# where F is the amount of the fine as described in the table above.

'''
1 to 20 -> 100
21 to 30 -> 270
31 and above -> 500
'''
speed_limit = int(input('Enter the speed limit: '))
speed = int(input('Enter the recorded speed of the car: '))

if speed <= speed_limit: 
    print('Congratulations, you are within the speed limit!')

else:
    if speed - speed_limit <= 20:
        fine = 100
    elif speed - speed_limit <= 30:
        fine = 270
    else:
        fine = 500
    print('You are speeding and your fine is $' + str(fine) + '.')
