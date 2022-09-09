#CHALLENGE 3
ans = int(input('First Player:\nEnter a number between 10 and 49: '))
while ans < 10 or ans > 49:
  ans = int(input('Enter a number between 10 and 49: '))
factor = 99 - ans

frans = int(input('\nSecond Player:\nEnter a number between 50 and 99: '))
while frans < 50 or frans > 99:
  frans = int(input('Enter a number between 50 and 99: '))
  
hold = factor + frans
hun = int(str(hold)[0])
new = int(str(hold)[1::]) + hun
result = frans - new

print(f'\nI said the answer was {ans} and the calculation result is {result}')
