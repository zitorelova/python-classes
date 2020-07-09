def countdown_reg(i):
    count = i # create a variable and set the input to that variable
    while count >= 0: # keep checking if the count is greater than or equal to 0
        print(count) # print it
        count -= 1 # subtract 1 from the count


def countdown_rec(i):
    print(i) # print the input
    if i <= 0: # check if the input is less or equal to 0
        return
    countdown_rec(i - 1)

countdown_rec(5)