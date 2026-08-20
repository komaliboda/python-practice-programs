# Access values from a nested dictionary using a loop

student = {
    "student1":{
        "name":"komali",
        "age":19
    },
    "student2":{
        "name":"vishnu",
        "age":20
    }
    }
for i in student:
    print(student[i])