#CHALLENGE 5 
def layers(x):
    stringg = str(x)
    return stringg[1::] + stringg[0]

def check(z,y):
    if int(goal) == int(layers(guess)):
        print('Your guess is correct.')
    else:
        print('Your guess in incorrect')
        print('Thanks for playing')
        
if __name__ == '__main__':
    print('Guess a six-digit number SLAYER so that following equation is true, where each letter stands for the diGit in th position shows: SLAYER + SLAYER + SLAYER = LAYERS.')

    guess = int(input('Enter your guess for SLAYER: '))
    while len(str(guess)) != 6:
        guess = int(input('Enter your guess for SLAYER: '))
    goal = guess * 3

    print(f'SLAYER + SLAYER + SLAYER = {goal}')
    print(f'LAYERS = {layers(guess)}')
    
    check(int(goal), int(layers(guess)))
