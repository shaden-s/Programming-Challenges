#CHALLENGE 18
from math import comb

def find(pos, length, password=""):
	alphnum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	if length == 0:
		return password
	start = (alphnum.index(password[-1])+1) if password else 0
	for letter in range(start, 36):
		holder = comb(36-(letter+1), length - 1)
		if holder >= pos:
			return find(pos, length - 1, password+alphnum[letter])
		pos -= holder
		
if __name__ == '__main__':
    pos = int(input('Enter position: '))
    length = 1
    while comb(36, length) < pos:
     pos -= comb(36,length)
     length += 1
    print(find(pos,length))