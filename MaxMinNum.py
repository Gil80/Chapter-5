# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the biggestimum and smallestimum of the numbers instead of the average.

biggest = 0
smallest = 0
print('biggest Before:', biggest)
print('smallest Before:', smallest)

while True:
    itervar = input('Type a number > ')
    if itervar == 'done':
        break
    try:
        itervar = int(itervar)  # checking if the input is an integer
    except:
        print('Invalid Input')
        continue
    if itervar > biggest:
        biggest = itervar
        print('Loop biggest:', itervar, biggest)
        continue
    elif smallest == 0 or itervar < smallest:
        smallest = itervar
        print('Loop smallest:', itervar, smallest)
        continue

print('biggest:', biggest, 'smallest:', smallest)
