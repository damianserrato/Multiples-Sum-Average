# Part one: Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

for count in range(1, 1001,2): # this line indicates what the variable count should loop up to, starting from 1, 1001 times, it will count only odd numbers
    print count                # this line tells the loop to print the value each time the counter goes up

# Part 2: Create another program that prints all the multiples of 5 from 5 to 1,000,000

for count in range(5, 1000001): # this line is saying that we should count starting at 5, up to 1,000,000
    if count % 5 == 0:          # here we create our if statement saying that if the current number is divisible by 5, 
        print count             # we can go ahead and print the current number

# Sum List: Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1,2,5,10,255,3] # setting a variable for our list
mySum = 0            # setting a variable for our final sum

for count in range(0, len(a)): # Here we're saying that our for loop should loop until the index reaches the length of the list
    mySum += a[count]          # We set mySum to be equal to MySum plus the current value of count
print mySum                    # After the loop is done, we output the value of mySum, which is the sum of tall the values within the list

# Average List: Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
thisSum = 0

for count in range(0, len(a)): # This is basically the same function as before, only we divide the result by the number of values in the list to get the average
    thisSum += a[count]
print thisSum / len(a)

