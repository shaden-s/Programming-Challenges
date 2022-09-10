#CHALLENGE 6
order = int(input('Input the order of the square: '))
topleft = int(input('Input the top left of the sqaure: '))

while topleft >= order:
  print('The top left number must be between 1 and the first number entered.')
  topleft = int(input('Input the top left of the sqaure: '))

lines = []
c = topleft
for x in range(order):
  for x in range(order + 1):
    if c <= order:
      lines.append(str(c))
      c += 1
    else:
      c = 1
  c += 1


print('This is your Latin Square:\n')
d=0
for x in range(order):
  str=''
  for i in range(order):
    str += lines[d] + ' '
    d+=1
  print(str)
    