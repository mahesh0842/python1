import csv
f = open('/Users/maheshyadav/Documents/python/OSMODULEOPERATIO/students.csv', 'r')
csv_reader = csv.reader(f)
next(csv_reader)  # Skip the header row
"""for row in csv_reader:
    print(row[2])"""
 
agee=[]
for row in csv_reader:
    agee.append(row[2])
print("minimum age is:", min(agee))
print("maximum age is:", max(agee))
print("average age is:", sum(map(int, agee)) / len(agee))
print("total number of students:", len(agee))
print("total number of students with age 20:", agee.count('20'))
f.close()