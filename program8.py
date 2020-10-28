
mat= [
    [1,2,3],
    [4,5,6]
]
#1st code to show matrix:
for x in mat:
    print(x)
#2nd code to show matrix:
for row in mat:
    for col in row:
        print(col)
#which is efficient??

studentid = {
    "101" : "Ruhul Amin",
    "102" : "Naim",
    "103" : "Arin"
}
print(studentid.get("101","Not a valid key."))

students = (
    "Ruhul Amin",
    "Naim Amin",
    "Ruhul Arin",
)

print(students[2])
print(students[1:])
print(students)