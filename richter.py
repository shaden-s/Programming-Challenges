#CHALLENGE 2
richter = float(input('Enter Richter scale value: '))

def energy(i):
  return 10**((1.5*i) + 4.8)
def tnt(k):
  return energy(k) / 4184000000

def present(r):
  print(f'\n{r}          {energy(r)}          {tnt(r)}\n')

print('\nRichter            Joules            TNT')
present(1)
present(5)
present(9.1)
present(9.2)
present(9.5)


print(f'Richter Value: {richter}\nEquivalence in Joules: {energy} \nEquivalence in tons of TNT: {tnt}')