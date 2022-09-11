#CHALLENGE 2
def energy(i):
  return 10**((1.5*i) + 4.8)
def tnt(k):
  return energy(k) / 4184000000

def present(r):
  print(f'\n{r:<12}{energy(r):<30}{tnt(r):<30}\n')
  
if __name__ == '__main__':
    richter = float(input('Enter Richter scale value: '))
    
    print('\nRichter     Joules                        TNT')
    present(1)
    present(5)
    present(9.1)
    present(9.2)
    present(9.5)


    print(f'Richter Value: {richter}\nEquivalence in Joules: {energy(richter)} \nEquivalence in tons of TNT: {tnt(richter)}')


