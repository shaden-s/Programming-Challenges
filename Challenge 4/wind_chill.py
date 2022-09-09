#CHALLENGE 4

def calculatewindchill(temp, speed):
  windchill = 35.74 + (0.6215 * temp) - (35.75 * speed**0.16) + (0.4275*temp*(speed**0.16))
  return windchill

def present(temp, speed):
  print(f'_______________________________________________\nTemperature: {temp}\nSpeed: {speed}\nWindchill: {calculatewindchill(temp, speed)}\n_______________________________________________')

present(10, 15)
present(0, 25)
present(-10, 35)
utemp = float(input('Enter Temperature: '))
uspeed = float(input('Enter Speed: '))
present(utemp, uspeed)
  
