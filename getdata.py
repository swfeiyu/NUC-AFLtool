"""
:file: getdata.py
:brief: To get values of user from conf.ini and processed these values
:version: 2.0
:author:SWfeiyu
:date: 2024.4.18
"""

from configparser import ConfigParser
from cal import *

"""
:name: GetData
:brief: To get values of user from conf.ini and processed these values
:return: Value -> Dict ={
                            "Name",
                            "StudentID",
                            "Class",
                            "Gender",
                            "AcademicYear",
                            "Semester",
                            "Days",
                            "StartTime":{"year","mon","day","hour","min","sec"}
                            "EndTime":{"year","mon","day","hour","min","sec"}
                            "CreationTime":{"year","mon","day","hour","min","sec"}
                            "ClosingTime":{"year","mon","day","hour","min","sec"}
                        }
"""
def GetData() -> Dict:
    config = ConfigParser()
    config.read("conf.ini")
    template = config.get("template", "template")

    flag=int(config.get(template, "flag"))
    Value = {}
    Value["Name"] = config.get(template, "Name")
    Value["StudentID"] = config.get(template, "StudentID")
    Value["Class"] = config.get(template, "Class")
    Value["Gender"] = config.get(template, "Gender")
    Value["AcademicYear"] = CalAcademicYear()
    Value["Semester"] = CalSemester()

    if flag != 10:
        Value["StartTime"] = CalStartTime(flag)
        Value["EndTime"] = CalEndTime(flag)
        Value["CreationTime"] = CalCreationTime(flag)
        Value["ClosingTime"] = CalClosingTime(flag)
    else:
        StartTime = {}
        EndTime = {}
        CreationTime = {}
        ClosingTime = {}

        StartTime["year"] = int(config.get(template, "StartTimeYear"))
        StartTime["mon"] = int(config.get(template, "StartTimeMon"))
        StartTime["day"] = int(config.get(template, "StartTimeDay"))
        StartTime["hour"] = int(config.get(template, "StartTimeHour"))
        StartTime["min"] = int(config.get(template, "StartTimeMin"))
        StartTime["sec"] = 0
        EndTime["year"] = int(config.get(template, "EndTimeYear"))
        EndTime["mon"] = int(config.get(template, "EndTimeMon"))
        EndTime["day"] = int(config.get(template, "EndTimeDay"))
        EndTime["hour"] = int(config.get(template, "EndTimeHour"))
        EndTime["min"] = int(config.get(template, "EndTimeMin"))
        EndTime["sec"] = 0
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
    Value["Days"] = CalDays(flag, Value)

    return Value

