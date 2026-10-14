# Write student details into a CSV file using csv.writer()

import csv

with open("student.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["name","age","marks"])
    writer.writerow(["komu",19,90])
    writer.writerow(["vishnu",20,91])