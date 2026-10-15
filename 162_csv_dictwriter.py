# Write dictionary data into a CSV file using csv.DictWriter()

import csv

with open("student.csv","w") as file:
    writer = csv.DictWriter(file,fieldnames = ["name","age","marks"])
    writer.writeheader()
    writer.writerow({"name":"komu","age":19,"marks":90})
    writer.writerow({"name":"vishnu","age":20,"marks":92})