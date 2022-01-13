#3 more decision problems
#FizzBuzz values
#use % to find multiples of a numner equaled to zero

number = int(input('Enter a positive integer: '))

if number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
elif number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
else:
    print(number)

#Another way to do this question
#this way isn't good because it doesnt have elif or else

number_str = ''
if number % 3 == 0:
    number_str += 'Fizz'
if number % 5 == 0:
    number_str += 'Buzz'
if number_str == '':
    number_str += str(number)
