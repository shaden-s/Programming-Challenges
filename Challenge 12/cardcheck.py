#CHALLENE 12

#FUNCTIONS
def checkalpha(num):
  flag = False
  for x in num:
    if x.isalpha():
      flag = True
  return flag
  
def checklenandalpha(cardnum):
  while len(cardnum) < 16:
    print('Too Short')
    cardnum = input('Enter Card No: ')
  while len(cardnum) > 16:
    print('Too Long')
    cardnum = input('Enter Card No: ')
  while checkalpha(cardnum):
    print('Has letters in it.')
    cardnum = input('Enter Card No: ')
  return cardnum

def digit_add(digit):
  if digit < 10:
    return digit
  else:
    return (digit % 10) + (digit // 10)

def double_list(num):
  list = []
  c = 1
  while c != len(num)+1:
    if c % 2:
      list.append(num[c-1]*2)
    else:
      list.append(num[c-1])
    c += 1
  return list
  
def luhn(num):
  checksum = int(num[-1])
  num = [int(x) for x in num[:-1]][::-1]
  doubles = double_list(num)
  doob = [digit_add(x) for x in doubles]
  return 10-(sum(doob) % 10) == checksum

def issuer(num):
  identity = ''
  if num[:2] in ['34', '37']:
    identity = 'American Express'
  elif num[:2] in ['51','52','53','54','55']:
    identity = 'Mastercard'
  elif num[0] == '4':
    identity = 'Visa'
  if num[0] == '3':
    identity = 'JCB'
  return identity
#MAIN LOOP
if __name__ == '__main__':
  dash = '-' * 20
  
  cardno = input('Enter Card No: ')
  cardno = checklenandalpha(cardno)

  if luhn(cardno):
    print(f'{dash}\nCard is valid')
    print(f'{dash}\nCard Issuer: {issuer(cardno)}\n{dash}')
  else:
    print('Card is not valid.')