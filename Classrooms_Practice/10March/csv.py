import csv
from datetime import date
file=open('expense.csv','a+',newline='')
file.seek(0)
r=csv.reader(file)
print(list(r))
