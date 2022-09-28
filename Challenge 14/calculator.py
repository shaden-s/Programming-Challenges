#CHALLENGE 14
def calculate(str):
  if str[2] == '+':
    return int(str[0]) + int(str[1])
  elif str[2] == '-':
    return int(str[0]) - int(str[1])
  elif str[2] == '*':
    return int(str[0]) * int(str[1])
  elif str[2] == '**':
    return int(str[0]) ** int(str[1])
  elif str[2] == '/':
    return int(str[0]) / int(str[1])
  elif str[2] == '//':
    return int(str[0]) // int(str[1])
  elif str[2] == '%':
    return int(str[0]) % int(str[1])

#MAIN LOOP
if __name__ == '__main__':
  calc = input('Enter your calculation: ').split(' ')
  
  while calc != ['q']:
    print(calculate(calc))
    calc = input('Enter your calculation: ').split(' ')
  print('Goodbye')
  quit()
