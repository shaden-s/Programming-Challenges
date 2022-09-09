#CHALLENGE 5 

print('Guess a six-digit number SLAYER so that following equation is true, where each letter stands for the diGit in th position shows: SLAYER + SLAYER + SLAYER = LAYERS.')

guess = int(input('Enter your guess for SLAYER: '))
while len(str(guess)) != 6:
  guess = int(input('Enter your guess for SLAYER: '))
goal = guess * 3

stringg = str(guess)
layers = stringg[1::] + stringg[0]

print(f'SLAYER + SLAYER + SLAYER = {goal}')
print(f'LAYERS = {layers}')

if int(goal) == int(layers):
  print('Your guess is correct.')
else:
  print('Your guess in incorrect')
print('Thanks for playing')
