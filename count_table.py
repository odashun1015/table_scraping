import csv
f = open('hoge.csv')
dataReader=csv.reader(f)
count=0
for row in dataReader:
	print(str(row).split())
	count=count+len(str(row).split())
print(count)	
