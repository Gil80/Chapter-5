# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead of the average.

max = None
min = None
print('Max Before:', max)
print('Min Before:', min)

while True:
    itervar = input('Type a number > ')
    if itervar == 'done':
        break
    elif itervar > max:
        max = itervar
        print('Loop:', itervar, max)
    continue
    try:
        itervar = int(itervar)  # checking if the input is an integer
    except:
        print('Invalid Input')
    continue

print('max:', max)
