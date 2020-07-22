
import pandas as pd
import random

class Student():
    def __init__(self):
        self.studInfo = list() #includes student name and scores

class Classroom():
    def __init__(self):
        self.studList = list() #list of students in the given class

classData = pd.read_csv("/Users/aleeml/Google Drive/Programming/Workspace/Python/Pops Projects/ClassroomData.csv", header = 0)
classA = Classroom()
classB = Classroom()
classC = Classroom()
school =    { #puts all classes into a dictionary
            "ClassA" : classA,
            "ClassB" : classB,
            "ClassC" : classC
            }
for i in range(30):
    student = Student()
    student.studInfo = classData.iloc[i]
    classroom = Classroom()
    if (i < 10):
        classroom = classA
    elif (i < 20):
        classroom = classB
    else:
        classroom = classC
    classroom.studList.append(student) #adds student to the appropriate class studList

subject = random.randrange(1, 6) #picks a random subject A-E akak columns 1-5
randomClass = random.choice(["ClassA", "ClassB", "ClassC"]) #returns one of the classroom objects from the dictionary 'school'
classesToTest = list()
classesToTest = ("ClassA", "ClassB", "ClassC")
testedStudents = list()

for classToTest in classesToTest:
    pickedClassroom = school[classToTest]
    print("\n" + classToTest)
    pickedStudents = list() #list of tuples of each selected student and their appropriate subject score
    while (len(pickedStudents) < 3):
        potStud = pickedClassroom.studList[random.randrange(10)]
        if (potStud.studInfo[0], potStud.studInfo[subject]) not in pickedStudents:
            pickedStudents.append((potStud.studInfo[0], potStud.studInfo[subject])) #in case a student is picked twice
            testedStudents.append((potStud.studInfo[0], potStud.studInfo[subject]))

    print("Subject:", list(classData.columns)[subject])
    for i in pickedStudents: #prints the student names and corresponding subject score
        print(i[0], i[1])

    max = list() #list of tuples of the students with the  highest scores
    min = list()
    avg = pickedStudents[0][1]
    max.append(pickedStudents[0]) #adds the first student to the list
    min.append(pickedStudents[0])
    for i in pickedStudents[1:]: #only considers the second and third list values
        avg += i[1]
        if (i[1] >= max[0][1]):
            if (i[1] > max[0][1]): #clears the list if the new student score is higher than the current max
                max.clear()
            max.append(i)

        if (i[1] <= min[0][1]):
            if (i[1] < min[0][1]):
                min.clear()
            min.append(i)

    print("Average:", round(avg/len(pickedStudents), 2))
    print("Maximum(s):")
    for i in max:
        print(i[0] + ":", i[1])
    print("Minimum(s):")
    for i in min:
        print(i[0] + ":", i[1])


max = list() #list of tuples of the students with the  highest scores
min = list()
avg = testedStudents[0][1]
max.append(testedStudents[0]) #adds the first student to the list
min.append(testedStudents[0])
for i in testedStudents[1:]: #only considers the second and third list values
    avg += i[1]
    if (i[1] >= max[0][1]):
        if (i[1] > max[0][1]): #clears the list if the new student score is higher than the current max
            max.clear()
        max.append(i)

    if (i[1] <= min[0][1]):
        if (i[1] < min[0][1]):
            min.clear()
        min.append(i)

print("\nAverage:", round(avg/len(testedStudents), 2))
print("Maximum(s):")
for i in max:
    print(i[0] + ":", i[1])
print("Minimum(s):")
for i in min:
    print(i[0] + ":", i[1])