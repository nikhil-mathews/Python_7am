import csv

fields=[]
rows=[]

with open('./record.csv','r') as file:
    csvreader=csv.reader(file)

    fields=next(csvreader)

    for row in csvreader:
        rows.append(row)
    print(f"Total number of rows are :{csvreader.line_num}")

    for i in fields:
        print(i)

    for row in rows:
        for col in row:
            print(col)