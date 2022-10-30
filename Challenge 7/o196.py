#CHALLENGE 7
def palindrome(x):
  if str(x)[::-1] == str(x):
    return True
  else:
    return False

def revadd(f):
  return f + int(str(f)[::-1])

def checklych(y):
  c = 0
  while c < 70:
    if palindrome(y):
      return True
    else:
      c += 1
      y=revadd(y)
  return False

def mainloop(ione, itwo):
	palcount = 0
	lychrel = []
	nonlych = 0
	for i in range(ione, itwo+1):
		if palindrome(i):
			palcount += 1
		else:
			if checklych(revadd(i)):
				nonlych += 1
			else:
				lychrel.append(i)
    
	printer(lychrel, palcount, nonlych)

def printer(lych,pal,non):
	for x in lych:
		print(f'{x} is probably lychrel')
		print(f'Palindrome numbers: {pal}\nNot Lychrel numbers: {non}\nLychrel = {len(lych)}')
      
if __name__ == '__main__':
  start = int(input('Integer 1: '))
  end = int(input('Integer 2: '))
  
  mainloop(start,end)
