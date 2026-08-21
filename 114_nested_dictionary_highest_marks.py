# Find the student with the highest marks in a nested dictionary

s = {
    "student1":{"name":"komali",
        "age":19,"marks":80
    },
    "student2":{"name":"vishnu",
    "age":18,"marks":70
    }
}
h_marks = 0

for i in s:
    s_marks = s[i]["marks"]
    if s_marks > h_marks:
        h_marks = s_marks
print(h_marks)
