#CHALLEGE 15
import csv

def read_csv(csv_file):
  csv_contents = []
  with open(csv_file) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)              
    for row in reader:
      csv_contents.append(row)
  return csv_contents

def read_html(html_file):
  f = open(html_file, "rt")
  lines = f.read()
  return lines

def process(csv,html):
  splits = html.split(' ')
  c = 1
  for y in csv:
    word = 'name' + str(c)
    inital = 'initials' + str(c)
    link = 'link' + str(c)
    for x in splits:
        html = html.replace(word, y[2])
        html = html.replace(inital, y[1])
        html = html.replace(link, y[0])
    c += 1
  return html

def write_html(file,path, html):
  files = open(file,"w")
  files.write(path)
  files.close()

if __name__ == '__main__':
  html_file = read_html('south.html')
  csv_file = read_csv('south.csv')
  skoop = process(csv_file, html_file)
  write_html('south_final.html',skoop, html_file)

