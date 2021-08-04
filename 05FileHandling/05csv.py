'''
csv-> comma separated values
,
'''
import csv

# column/field names
fields=['name','age','rollno']

# data in rows
rows=[
    ['Nikhil',23,1],
    ['javeed',24,2],
    ['John',24,3]
]

with open('./record.csv','w') as file:
    csvwriter=csv.writer(file)

    csvwriter.writerow(fields)

    csvwriter.writerows(rows)