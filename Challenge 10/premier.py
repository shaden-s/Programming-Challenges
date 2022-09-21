#CHALLENGE 10
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

def points(team, list, dict):
  numbers = []
  points = 0
  wins = 0
  draws = 0
  losses = 0
  scored = 0
  conceded = 0
  for row in list:
    if row[1] == team:
      if row[5] == 'H':
        points += 3
        wins += 1
      elif row[5] == 'D':
        points += 1
        draws += 1
      else:
        losses += 1
      scored += int(row[3])
      conceded += int(row[4])
      
    if row[2] == team:
      if row[5] == 'A':
        points += 3
        wins += 1
      elif row[5] == 'D':
        points += 1
        draws += 1
      else:
        losses += 1
      scored += int(row[4])
      conceded += int(row[3])
      
    diff = scored - conceded
    
  numbers.append([points, wins, draws,losses,diff])
  dict[team] = numbers

def accuracy(team, list, dict):
  teamshots = 0
  teamtarget = 0
  for row in list:
    if row[1] == team:
      teamshots += int(row[7])
      teamtarget += int(row[9])
    if row[2] == team:
      teamshots += int(row[8])
      teamtarget += int(row[10])
  acc = teamtarget / teamshots
  dict[team] = acc

def clean(team, list, dict):
  fouls = 0
  for row in list:
    if row[1] == team:
      fouls += int(row[11])
    if row[2] == team:
      fouls += int(row[12])
  dict[team] = fouls

def ref_stats(ref, list, dict):
  cardavg = 0
  for row in list:
    if row[6] == ref:
      cardavg += int(row[15]) + int(row[16])
      cardavg += 2 * (int(row[17]) + int(row[18]))
  dict[ref] = cardavg
  
def refs(content):
  return list(set([x[6] for x in content]))

def teams(content):
  return list(set([x[1] for x in content]))

def present(x, str):
  xs = max(x, key=x.get)
  ys = min(x, key=x.get)
  print(f'{line}\nMost {str}: {xs}\nLeast {str}: {ys}')
#VARIABLES

tableofpoints = {}
accuracies = {}
fouls = {}
ref_st = {}

#MAIN CODE
if __name__ == "__main__":
    content = read_csv('Premier 16-17.csv')
    teams = teams(content)
    refs = refs(content)
  
    for x in teams:
      points(x, content, tableofpoints)
      accuracy(x, content, accuracies)
      clean(x, content, fouls)

    for x in refs:
      ref_stats(x, content, ref_st)
      
    line = '-' * 40
    print(f'{line}\nPREMIER LEAGUE 16-17 TABLE\n{line}\n')
    print(f'Team             Points  W   D   L   G-D\n{line}')

    sorttabled = sorted(tableofpoints.items(), key=lambda item: item[1][0][0])

    state = True
    p = 1
    while state:
      for x in (sorttabled)[::-1]:
        print(f'{p:<3}{x[0]:<18}{x[1][0][0]:<4}{x[1][0][1]:<4}{x[1][0][2]:<4}{x[1][0][3]:<4}{x[1][0][4]:<4}')
        p += 1
      state=False

    present(accuracies, 'Accurate Team')
    present(fouls, 'Clean Team')
    present(ref_st, 'Cards per game by referee')
