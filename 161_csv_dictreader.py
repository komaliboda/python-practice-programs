# Read student records using csv.DictReader() and access values by column names

import csv

with open("student.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["names", "age", "marks"])
    writer.writerow(["komali",19,90])
    writer.writerow(["vishnu",20,92])

with open("student.csv","r") as file:
    read = csv.DictReader(file)
    for row in read:
        print(row)
        print(row["names"])