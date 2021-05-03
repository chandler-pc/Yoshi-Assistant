import datetime
import csv
import webbrowser

ddn = datetime.datetime.now()
hr = ddn.hour
mn = ddn.minute
day = datetime.datetime(ddn.year,ddn.month,ddn.day).strftime("%w")
h = []
links = []

with open('D:/Archivos/yoshi/anotherComms/csv/horario.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        h.append(row['h'])
        links.append(row[day])
i = 0
for x in h:
    if(int(x)==hr and links[i] != " "):
        webbrowser.open_new_tab(links[i])
        break
    i += 1