#PROJECT 1
def start():
  rods = float(input('Input Rods: '))
  return rods

def metres(input):
  return input * 5.0292

def furlong(input):
  return input / 40

def mile(input):
  metre = metres(input)
  return metre / 1609.34

def foot(input):
  metre = metres(input)
  return metre / 0.3048

def avgwalk(input):
  miles = mile(input)
  hours = (miles / 3.1) * 60
  return hours

def result(input):
  print(f'You input {input} rods.')
  print('Conversions')
  print(f'Meters: {metres(input)}')
  print(f'Feet: {foot(input)}')
  print(f'Miles: {mile(input)}')
  print(f'Furlongs: {furlong(input)}')
  print(f'Minutes to walk {input} rods: {avgwalk(input)}')

if __name__ == "__main__":
  result(start())
  
