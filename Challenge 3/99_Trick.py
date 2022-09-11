#CHALLENGE 3
def minusnine(x):
    return 99 - x

def result(i,j):
    return j - (int(str(i + j)[1::]) + int(str(i + j)[0]))

if __name__ == '__main__':
    ans = int(input('First Player:\nEnter a number between 10 and 49: '))
    while ans < 10 or ans > 49:
        ans = int(input('Enter a number between 10 and 49: '))
    factor = minusnine (ans)

    frans = int(input('\nSecond Player:\nEnter a number between 50 and 99: '))
    while frans < 50 or frans > 99:
        frans = int(input('Enter a number between 50 and 99: '))
  
    print(f'\nI said the answer was {ans} and the calculation result is {result(factor,frans)}')

