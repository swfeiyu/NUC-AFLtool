"""
:file: display.py
:brief: For displaying and getting values in the terminal
:version: 1.1
:author: SWfeiyu
:date: 2024.3.27
"""

from cal import *

"""
:name: Display
:brief: To display and get the name, studentID, classID, gender and the flag
:return: InputValue -> Dict ={"Name","StudentID","Class","Gender","flag"}
"""
def Display() -> Dict:
    InputValue = {}
    print("****NUC-AFLtool*****")
    InputValue["Name"] = input("Please enter your name:")
    InputValue["StudentID"] = input("Please enter your student ID:")
    InputValue["Class"] = input("Please enter your class ID:")
    InputValue["Gender"] = input("Please enter your gender:(m/w)")

    print("******************************")
    print("At what time are you going to take time off?(Please enter a serial number)")
    print("0.Morning Reading time")
    print("1.First class in the morning")
    print("2.Second class in the morning")
    print("3.First class in the afternoon")
    print("4.Second class in the afternoon")
    print("5.The class in the evening")
    print("6.All morning(Morning reading is included)")
    print("7.All afternoon(The class is included)")
    print("8.All day")
    print("9.All week")
    print("10.Customize")
    InputValue['Flag'] = int(input())

    return InputValue

"""
:name: GetValue
:brief: To get all values from cal.py or input
:return: Value -> Dict ={
                            "Name",
                            "StudentID",
                            "Class",
                            "Gender",
                            "AcademicYear",
                            "Semester",
                            "Days",
                            "StartTime":{"year","mon","day","hour","min","sec"},
                            "EndTime":{"year","mon","day","hour","min","sec"},
                            "CreationTime":{"year","mon","day","hour","min","sec"},
                            "ClosingTime":{"year","mon","day","hour","min","sec"},
                        }
"""
def GetValue() -> Dict:
    InputValue = Display()
    Value = {
        "Name": InputValue["Name"],
        "StudentID": InputValue["StudentID"],
        "Class": InputValue["Class"],
        "Gender": InputValue["Gender"],
        "AcademicYear": CalAcademicYear(),
        "Semester": CalsSemester()
    }

    if InputValue["Flag"] != 10:
        Value["StartTime"] = CalStartTime(InputValue["Flag"])
        Value["EndTime"] = CalEndTime(InputValue["Flag"])
        Value["CreationTime"] = CalCreationTime(InputValue["Flag"])
        Value["ClosingTime"] = CalClosingTime(InputValue["Flag"])
    else:
        StartTime = {}
        EndTime = {}
        CreationTime = {}
        ClosingTime = {}

        StartTime["year"] = int(input("Please enter the year of start time:"))
        StartTime["mon"] = int(input("Please enter the month of start time:"))
        StartTime["day"] = int(input("Please enter the day of start time:"))
        StartTime["hour"] = int(input("Please enter the hour of start time:"))
        StartTime["min"] = int(input("Please enter the minute of start time:"))
        StartTime["sec"] = random.randint(0, 60)
        EndTime["year"] = int(input("Please enter the year of end time:"))
        EndTime["mon"] = int(input("Please enter the month of end time:"))
        EndTime["day"] = int(input("Please enter the day of end time:"))
        EndTime["hour"] = int(input("Please enter the hour of end time:"))
        EndTime["min"] = int(input("Please enter the minute of end time:"))
        EndTime["sec"] = random.randint(0, 60)
        CreationTime["year"] = StartTime["year"]
        CreationTime["mon"] = StartTime["mon"]
        CreationTime["day"] = StartTime["day"]
        CreationTime["hour"] = StartTime["hour"] - 1
        CreationTime["min"] = random.randint(0, 60)
        CreationTime["sec"] = random.randint(0, 60)
        ClosingTime["year"] = StartTime["year"]
        ClosingTime["mon"] = StartTime["mon"]
        ClosingTime["day"] = StartTime["day"]
        ClosingTime["hour"] = StartTime["hour"] + 1
        ClosingTime["min"] = random.randint(0, 60)
        ClosingTime["sec"] = random.randint(0, 60)

        Value["StartTime"] = StartTime
        Value["EndTime"] = EndTime
        Value["CreationTime"] = CreationTime
        Value["ClosingTime"] = ClosingTime
    Value["Days"] = CalDays(InputValue["Flag"], Value)

    return Value

