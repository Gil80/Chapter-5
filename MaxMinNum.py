# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead of the average.

max = None
min = None
print('Max Before:', max)
print('Min Before:', min)

while True:
    itervar = input('Type a number> ')
    if input == 'done':
        break
    for itervar in itervar:
        if max is None or itervar > max:
            max = itervar
        print('Loop:', itervar, max)
    continue

print('max:', max)

'''   try:
        line = int(usr_input)  # checking if the input is an integer
    except:
        print('Invaid input')
        continue  # skip loop iteration and jump back to beginning of loop'''
