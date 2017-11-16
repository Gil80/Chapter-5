# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try
# and except and print an error message and skip to the next number.

count = 0
total = 0
avg = 0

while True:
    line = input('> ')
    if line == 'done':
        break
    try:
        line = int(line)  # checking if the input is an integer
    except:
        print('Invaid input')
        continue  # skip loop iteration and jump back to beginning of loop
    count = count + 1
    total = total + int(line)  # casting input type to an integer
    avg = total / count

print('Count:', count, 'total:', total, 'Average:', avg)