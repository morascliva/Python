

#students = ["Hermoine","Harry","Ron"]

#print(students[0])
#print(students[1])
#print(students[2])



#students = ["Hermoine","Harry","Ron"]

#for student in students:
#    print(student)



#students = ["Hermoine","Harry","Ron"]
#for i in range(len(students)):
#    print(i+1,students[i])



# using dictionaries 
#    
#students = {
#     "Harmione" : "Gryffindor",
#     "Harry":"Gryffindor",
#     "Ron" :"Gryffindor",
#    "Draco":"Slytherin",
# } 

#print(students["Harmione"])
#print(students["Draco"])

#for student in students:
 #   print(student,students[student],sep=",")


#list of dictionaries 
students =[
    {"name":"Harmione","house":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack"},
    {"name":"Draco","house":"Slytherine","patronus":None},

]

for student in students:
    print(student["name"],student["house"],student["patronus"],sep=",")
