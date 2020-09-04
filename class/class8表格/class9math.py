import csv
#csv表格地址
filename = '/Users/Administrator/Desktop/class9表格/math.csv'
with open(filename) as f:
    reader =  csv.reader(f)
    for row in reader:
        print(row)
