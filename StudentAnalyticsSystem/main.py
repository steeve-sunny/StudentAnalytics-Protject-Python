# add a class to store friendhsip
class Friendship(object):
    def __init__(self):
        self.d = {}

    def AddFriendship(self):
        # mapping the friendship with each other
        # values of keys are their friends
        with open("friendship.txt") as file:
            for line in file:
                line = line.strip().split()

                if line[0] in self.d and line[1] in self.d:
                    self.d[line[0]].append(line[1])
                    self.d[line[1]].append(line[0])
                
                elif line[0] not in self.d and line[1] not in self.d:
                    self.d[line[0]] = [line[1]]
                    self.d[line[1]] = [line[0]]
                
                elif line[1] in self.d and line[0] in self.d:
                    self.d[line[1]].append(line[0])
                    self.d[line[0]].append(line[1])
                
                elif line[0] in self.d and line[1] not in self.d:
                    self.d[line[0]].append(line[1])
                    self.d[line[1]] = [line[0]]
                
                elif line[1] in self.d and line[0] not in self.d:
                    self.d[line[1]].append(line[0])
                    self.d[line[0]] = [line[1]]
        return self.d
    
    def GetFriend(self, code):
        if code in self.d:
            return self.d[code]
        elif code == self.d[code]:
            return f"{code} has no friends but themselves"
    
    def __str__(self):
        # need to get the dictionary with the friendship and put them into human readable
        c = []
        for keys in self.d:
            c.append(f"Student: {keys} ------> Friends: {self.d[keys]}")
        return "\n".join(c)
            


# Getting the scores of students
class Student(object):
    # extracting the information from student_info.txt file 
    def __init__(self, sid=None, name=None, age=None, course=None):
        self.sid = sid if sid is not None else None
        self.name = name if name is not None else None
        self.age = age if age is not None else None
        self.course = course if course is not None else None

    score = {} 
    identification = {}
    average = {}
    year = {}
    degree = {}
    string_output = []
 
    def IdToStudent(self, sid, name):
        if sid not in self.identification:
            self.identification[sid] = name
        
    # we need a function that will return the name of student when given student ID
    def GetStudentName(self, sid):
        return self.identification[sid]

    # Function to store grades of students  
    def StoreGrade(self, sid, grade):
        if sid not in self.score:
            self.score[sid] = [int(grade)]
        else:
            self.score[sid].append(int(grade))
    
    # we need a function now to create to get the average of the students and return the student average
    def AverageGrade(self, sid):
        if sid in self.score:
            return sum(self.score[sid]) / len(self.score[sid])
        else:
            return f"Student {sid} doesn't have a grade"
    
    def AddAge(self, name, age):
        if self.name not in self.year:
            self.year[self.name] = self.age
    
    def GetAge(self, name):
        if name in self.year:
            return self.year[name]
        else:
            return f"This student is not enrolled and cannot get Age"
    
    def AddStudentToDegree(self):
        if self.name not in self.degree:
            self.degree[self.name] = self.course
    
    def GetStudentDegree(self, name):
        if name in self.degree:
            return self.degree[name]
        else:
            return f"The Student: {name} isn't valid and cannot extract degree"
    
    # we need to be able to print the output cleanly in terminal
    #thefore we need a clean string class in order to do that
    # to make it humman readable

    def __str__(self):
        return f"Name: {self.name}, ID: {self.sid}, Age: {self.age}, Course: {self.course}"
       

# this is for the terminal output, to look cleaner on terminal
print("\n" + "="*50) # newline after code run and then 50 of them symbols
print("       STUDENT ANALYTICS REPORT") # text in middle and in the centre of both the symbols
print("="*50) # just 50 of them symbols

# need to assign the Student class based on the information in the following file.
try:
    with open("Student_info.txt") as f:
        StoreStudentClass = {}
        AllStudents = set()
        try:
            for line in f:
                line = line.strip().split(",")
                sid, name, age, course = line[0], line[1], line[2], line[3]
                AllStudents.add(line[1])
                s = Student(sid, name, age, course)
                print(s)
                StoreStudentClass[sid] = s
                s.IdToStudent(sid, name)
                s.AddAge(name, age)
                s.AddStudentToDegree()
        except ValueError:
            print(f"The line {line} is not a correct value")
except FileNotFoundError:
    print(f"The File Student_info.txt doesn't exist")


# we open the grades file to store each students grade by assigning it to the StudentID
try:
    with open("grades.txt") as file:
        for line in file:
            line = line.strip().split(",")
            sid, g = line[0], line[1]       # g is used for grade.
            s.StoreGrade(sid, g)
except FileNotFoundError:
    print(f"The File grades.txt doesn't exist")


f = Friendship()
f.AddFriendship()

# the commented code underneath is for to search up specific details , instead of having everthing printed, especially 1000s of input
# it's a tool for lookup, uncomment in order to check information needed


#print(f.GetFriend("S002")), #it gets the friends of the code given, need to provide ID.
#print(s.AverageGrade("S002")),  #it works amd gets the averag age after give the code, need to provide ID. , need to fix this 
#print(s.GetStudentName("S002")), # gets the name of the student entered, need to provide ID.
#print(s.GetAge("Sarah ONeill")) # gets the age of the student entered, need student ID.
#print(s.GetStudentDegree("John Murphy")) # gets the students degree, student name needed.
#print(AllStudents) # stores all students, stored in list