import csv

with open('museum.csv', new='') as csvfile:
    artreader = csv.DictReader(csvfile, delimeter='|')
    rows = list(artreader)
    for each in rows[1:3]:
        print(each['group1'])