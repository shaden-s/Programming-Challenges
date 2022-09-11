#CHALLENGE 6
def generatelatin(order, c):
  lines = []
  for i in range(order):
    for x in range(order + 1):
      if c <= order:
        lines.append(str(c))
        c += 1
      else:
        c = 1
    c += 1
  return lines

def drawlatin(arr, order):
  d=0
  str = ''
  for x in range(order):
    for i in range(order):
      str += arr[d] + ' '
      d+=1
    str += '\n'
  return str
    
if __name__ == '__main__':
  order = int(input('Input the order of the square: '))
  topleft = int(input('Input the top left of the sqaure: '))

  while topleft >= order:
    print('The top left number must be between 1 and the first number entered.')
    topleft = int(input('Input the top left of the sqaure: '))

  latin = generatelatin(order, topleft)

  print(f'This is your Latin Square:\n{drawlatin(latin, order)}')
