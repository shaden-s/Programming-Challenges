#CHALLENGE 18
from itertools import permutations
def paintings(a, b, c, d):
  arts = a * 'A' + b * 'B' + c * 'C' + d * 'D'
  return [list(x) for x in sorted(set(permutations(arts)))]

def choose(list, n):
  return ' '.join(list[n-1])

if __name__ == '__main__':
  a = int(input('How many paintings by Artist A: '))
  b = int(input('How many paintings by Artist B: '))
  c = int(input('How many paintings by Artist C: '))
  d = int(input('How many paintings by Artist D: '))
  n = int(input('Which arrangment: '))
  gallery = paintings(a,b,c,d)
  print(choose(gallery, n))
