# Write student records to a CSV file and read them row by row

import csv

with open("student.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["names", "age", "marks"])
    writer.writerow(["komali",19,90])
    writer.writerow(["vishnu",20,92])

with open("student.csv","r") as file:
    read = csv.reader(file)
    for row in read:
        print(row)
