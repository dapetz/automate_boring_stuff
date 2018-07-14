# The Collatz Sequence

# Logic for the collatz sequence
def collatz(number):
    global result
    if number % 2 == 0:
        print(str(number // 2))
        result = number // 2
        return result
    elif number % 2 == 1:
        print(str(3 * number + 1))
        result = 3 * number + 1
        return result

# Ask user to input a number
count = 0
print('Enter number:')
try:
    number = int(input())
except ValueError:
    print('The value must be an integer!')

#Execute the sequence. Print each value in the sequence the total iterations to solve
while number !=1:
    collatz(number)
    number = result
    count = count + 1
    continue
print('Collatz Sequence ran for ' + str(count) + ' iterations')
