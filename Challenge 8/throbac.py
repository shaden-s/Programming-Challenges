#CHALLENGE 8
def numerals(l):
  n = 0
  if l == 'I':
    n = 1
  elif l == 'V':
    n = 5
  elif l == 'X':
    n = 10
  elif l == 'L':
    n = 50
  elif l == 'C':
    n = 100
  return n

def romtonum(rom):
  holder = 0
  x = 0
  state = True
  while state:
    if x < len(rom)-1: 
      if numerals(rom[x]) >= numerals(rom[x+1]):
        holder += numerals(rom[x])
      else:
        holder += numerals(rom[x+1]) - numerals(rom[x])
        x += 1
    else:
      if x == len(rom)-1:
        if numerals(rom[x]) <= numerals(rom[x-1]):
          holder += numerals(rom[x])
      state = False
    x += 1
  return holder

def numtorom(number):
  letter =  ''
  num = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
  sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
  i = 12
      
  while number:
    div = number // num[i]
    number %= num[i]
  
    while div:
      letter += sym[i]
      div -= 1
    i -= 1
  return letter

if __name__ == "__main__":
  rom_one = input('Enter First Roman Number (no spaces): ').upper()
  rom_two = input('Enter Second Roman Number (no spaces): ').upper()
  
  num_one = (romtonum(rom_one))
  print(f'Value of {rom_one}: {num_one}')
  num_two = (romtonum(rom_two))
  print(f'Value of {rom_two}: {num_two}')
  
  ans = (num_one+num_two)
  print(f'Digital Sum is: {ans}')
  print(f'Roman Sum is: {numtorom(ans)}')
