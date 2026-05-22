🔍 Overview: 
The Student Analytics System ingests structured text files to store and query student data. It models two core entities — students and friendships — allowing use 
to look up grades, averages, demographics, and social connections by student ID.


✨ Features:
 1. 📊 Grade Tracking — stores multiple grades per student and computes averages
 2. 🧑‍🎓 Student Profiles — name, ID, age, and enrolled course per student
 3. 🤝 Friendship Graph — bidirectional social graph built from relationship data
 4. 🔎 Lookup Utilities — query any student by ID or name
 5. 🛡️ Error Handling — graceful handling of missing files and malformed data



📄 Data File Formats:
 1. Student_info.txt — comma-separated student records:
    S001,John Murphy,20,Computer Science

 2. grades.txt — student ID mapped to a grade (multiple entries per student supported):
    S001,85
    S001,90

 3. friendship.txt — space-separated student ID pairs (bidirectional):
    S001 S002



💻 Lookup Usage:
Uncomment any of the following in main.py for targeted queries:
python

print(f.GetFriend("S002"))           # Friends of a student
print(s.AverageGrade("S002"))        # Student's grade average
print(s.GetStudentName("S002"))      # Name from ID
print(s.GetAge("Sarah ONeill"))      # Student's age
print(s.GetStudentDegree("John Murphy"))  # Enrolled degree



🏗️ Class Architecture:
1. Student — handles all academic and demographic data

Method                                Description
StoreGrade(sid, grade)                Appends a grade to a student's record
AverageGrade(sid)                     Returns the student's grade average
GetStudentName(sid)                   Returns name from student ID
GetAge(name)                          Returns age of a named student
GetStudentDegree(name)                Returns enrolled course

2. Friendship — models peer network as an adjacency-list graph

Method                                Description
AddFriendship()                       Parses file and builds bidirectional friendship map
GetFriend(code)                       Returns friend list for a given student ID



👤 Author
Steeve Sunny — https://github.com/steeve-sunny · LinkedIn

