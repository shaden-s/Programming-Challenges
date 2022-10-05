months = {'JAN': 1, 'FEB':2, 'MAR':3, 'APR':4,'MAY':5, 'JUN':6,'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12}

def SplitDate(date):
  date[1] = months[date[1]]
  return tuple(date)

def histogram(word):
  hist = {}
  for x in word:
    hist[x] = word.count(x)
  return sorted(hist.items(), key=lambda item: item[1])[::-1]
  

if __name__ == '__main__':
  date = input('Enter date:').split('-')
  print(SplitDate(date))

  word = input('Enter Word: ')
  for x in histogram(word):
    print(f'The letter {x[0]} appears {x[1]} time.')
