#CHALLENGE 11
import csv
#FUNCTIONS
def read_csv(csv_file):
  csv_contents = []
  with open(csv_file) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)              
    for row in reader:
      csv_contents.append(row)
  return csv_contents

def addtotal(date, content, dict):
  total_volume = 0.0
  total_sales = 0.0
  for x in content:
    if x[0].split('-')[:2] == date:   
      total_volume += float(x[6])
      total_sales += float(x[5]) * float(x[6])
  dict['-'.join(date)] = [total_sales,total_volume, (total_sales/total_volume)]
      

def alldates(content):
  return [list(x) for x in list(set([tuple(x[0].split('-')[:2]) for x in content]))]

#MAIN LOOP
if __name__ == '__main__':
  contents = read_csv('AAPL.csv')
  dates = alldates(contents)
  
  volumes = {}
  for x in dates:
    addtotal(x, contents,volumes)
    
  vol2 = sorted(volumes.items(), key=lambda e: e[1][2])[::-1]
  topsix = vol2[:6]
  bottomsix = vol2[-6:][::-1]

  dash = '-'*10
  print(f'{dash}\nTOP 6\n{dash}')
  for x in topsix:
    print(f'{x[0]:<7} -> {x[1]}')

  print(f'{dash}\nBOTtOM 6\n{dash}')
  for x in bottomsix:
    print(f'{x[0]:<7} -> {x[1]}')
