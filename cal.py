"""
:file: cal.py
:brief: For calculating some values used by application
:version: 1.0
:author: SWfeiyu
:date: 2024.1.31
"""

import random
import time
from typing import Dict

"""
:name: CalAcademicYear
:brief: According to current month to calculate the academic year
:return: AcademicYear -> int
"""
def CalAcademicYear() -> int:
    if 8 < time.localtime(time.time()).tm_mon <= 12:
        return time.localtime(time.time()).tm_year
    else:
        return time.localtime(time.time()).tm_year - 1

"""
:name: CalSemester
:brief: According to current month to calculate the semester
:return: Semester -> int
"""
def CalsSemester() -> int:
    if 2 <= time.localtime(time.time()).tm_mon <= 7:
        return 2
    else:
        return 1

"""
:name: CalStartTime
:brief: According to the flag to calculte the start time
:param: flag -> int
:return: StartTime -> Dict ={"year","mon","day","hour","min","sec"}
"""
def CalStartTime(flag: int) -> Dict:
    StartTime = {}
    if flag == 0 or flag == 6 or flag == 8:
        StartTime["year"] = time.localtime(time.time()).tm_year
        StartTime["mon"] = time.localtime(time.time()).tm_mon
        StartTime["day"] = time.localtime(time.time()).tm_mday
        StartTime["hour"] = 6
        StartTime["min"] = 40
        StartTime["sec"] = 0
    elif flag == 1:
        StartTime["year"] = time.localtime(time.time()).tm_year
        StartTime["mon"] = time.localtime(time.time()).tm_mon
        StartTime["day"] = time.localtime(time.time()).tm_mday
        StartTime["hour"] = 8
        StartTime["min"] = 0
        StartTime["sec"] = 0
    elif flag == 2:
        StartTime["year"] = time.localtime(time.time()).tm_year
        StartTime["mon"] = time.localtime(time.time()).tm_mon
        StartTime["day"] = time.localtime(time.time()).tm_mday
        StartTime["hour"] = 10
        StartTime["min"] = 10
        StartTime["sec"] = 0
    elif flag == 3 or flag == 7:
        StartTime["year"] = time.localtime(time.time()).tm_year
        StartTime["mon"] = time.localtime(time.time()).tm_mon
        StartTime["day"] = time.localtime(time.time()).tm_mday
        if 5 <= StartTime["mon"] < 10:
            StartTime["hour"] = 14
            StartTime["min"] = 0
            StartTime["sec"] = 0
        else:
            StartTime["hour"] = 14
            StartTime["min"] = 30
            StartTime["sec"] = 0
    elif flag == 4:
        StartTime["year"] = time.localtime(time.time()).tm_year
        StartTime["mon"] = time.localtime(time.time()).tm_mon
        StartTime["day"] = time.localtime(time.time()).tm_mday
        if 5 <= StartTime["mon"] < 10:
            StartTime["hour"] = 16
            StartTime["min"] = 10
            StartTime["sec"] = 0
        else:
            StartTime["hour"] = 16
            StartTime["min"] = 40
            StartTime["sec"] = 0
    elif flag == 5:
        StartTime["year"] = time.localtime(time.time()).tm_year
        StartTime["mon"] = time.localtime(time.time()).tm_mon
        StartTime["day"] = time.localtime(time.time()).tm_mday
        if 5 <= StartTime["mon"] < 10:
            StartTime["hour"] = 19
            StartTime["min"] = 0
            StartTime["sec"] = 0
        else:
            StartTime["hour"] = 19
            StartTime["min"] = 30
            StartTime["sec"] = 0
    elif flag == 9:
        StartTime["year"] = time.localtime(time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60).tm_year
        StartTime["mon"] = time.localtime(time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60).tm_mon
        StartTime["day"] = time.localtime(time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60).tm_mday
        StartTime["hour"] = 6
        StartTime["min"] = 40
        StartTime["sec"] = 0

    return StartTime

"""
:name: CalEndTime
:brief: According to the flag to calculte the end time
:param: flag -> int
:return: EndTime -> Dict ={"year","mon","day","hour","min","sec"}
"""
def CalEndTime(flag: int) -> Dict:
    EndTime = {}
    if flag == 0:
        EndTime["year"] = time.localtime(time.time()).tm_year
        EndTime["mon"] = time.localtime(time.time()).tm_mon
        EndTime["day"] = time.localtime(time.time()).tm_mday
        EndTime["hour"] = 7
        EndTime["min"] = 30
        EndTime["sec"] = 0
    elif flag == 1:
        EndTime["year"] = time.localtime(time.time()).tm_year
        EndTime["mon"] = time.localtime(time.time()).tm_mon
        EndTime["day"] = time.localtime(time.time()).tm_mday
        EndTime["hour"] = 9
        EndTime["min"] = 40
        EndTime["sec"] = 0
    elif flag == 2 or flag == 6:
        EndTime["year"] = time.localtime(time.time()).tm_year
        EndTime["mon"] = time.localtime(time.time()).tm_mon
        EndTime["day"] = time.localtime(time.time()).tm_mday
        EndTime["hour"] = 11
        EndTime["min"] = 50
        EndTime["sec"] = 0
    elif flag == 3:
        EndTime["year"] = time.localtime(time.time()).tm_year
        EndTime["mon"] = time.localtime(time.time()).tm_mon
        EndTime["day"] = time.localtime(time.time()).tm_mday
        if 5 <= EndTime["mon"] < 10:
            EndTime["hour"] = 15
            EndTime["min"] = 40
            EndTime["sec"] = 0
        else:
            EndTime["hour"] = 16
            EndTime["min"] = 10
            EndTime["sec"] = 0
    elif flag == 4 or flag == 7:
        EndTime["year"] = time.localtime(time.time()).tm_year
        EndTime["mon"] = time.localtime(time.time()).tm_mon
        EndTime["day"] = time.localtime(time.time()).tm_mday
        if 5 <= EndTime["mon"] < 10:
            EndTime["hour"] = 17
            EndTime["min"] = 50
            EndTime["sec"] = 0
        else:
            EndTime["hour"] = 18
            EndTime["min"] = 20
            EndTime["sec"] = 0
    elif flag == 5 or flag == 8:
        EndTime["year"] = time.localtime(time.time()).tm_year
        EndTime["mon"] = time.localtime(time.time()).tm_mon
        EndTime["day"] = time.localtime(time.time()).tm_mday
        if 5 <= EndTime["mon"] < 10:
            EndTime["hour"] = 21
            EndTime["min"] = 35
            EndTime["sec"] = 0
        else:
            EndTime["hour"] = 22
            EndTime["min"] = 5
            EndTime["sec"] = 0
    elif flag == 9:
        EndTime["year"] = time.localtime(
            time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60 + 4 * 24 * 60 * 60).tm_year
        EndTime["mon"] = time.localtime(
            time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60 + 4 * 24 * 60 * 60).tm_mon
        EndTime["day"] = time.localtime(
            time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60 + 4 * 24 * 60 * 60).tm_mday
        if 5 <= EndTime["mon"] < 10:
            EndTime["hour"] = 21
            EndTime["min"] = 35
            EndTime["sec"] = 0
        else:
            EndTime["hour"] = 22
            EndTime["min"] = 5
            EndTime["sec"] = 0

    return EndTime

"""
:name: CalCreationTime
:brief: According to the flag to calculte the creation time
:param: flag -> int
:return: CreationTime -> Dict ={"year","mon","day","hour","min","sec"}
"""
def CalCreationTime(flag: int) -> Dict:
    CreationTime = {}
    if flag == 0 or flag == 6 or flag == 8:
        CreationTime["year"] = time.localtime(time.time()).tm_year
        CreationTime["mon"] = time.localtime(time.time()).tm_mon
        CreationTime["day"] = time.localtime(time.time()).tm_mday
        CreationTime["hour"] = 6
        CreationTime["min"] = random.randint(20, 40)
        CreationTime["sec"] = random.randint(0, 60)
    elif flag == 1:
        CreationTime["year"] = time.localtime(time.time()).tm_year
        CreationTime["mon"] = time.localtime(time.time()).tm_mon
        CreationTime["day"] = time.localtime(time.time()).tm_mday
        CreationTime["hour"] = 7
        CreationTime["min"] = random.randint(0, 40)
        CreationTime["sec"] = random.randint(0, 60)
    elif flag == 2:
        CreationTime["year"] = time.localtime(time.time()).tm_year
        CreationTime["mon"] = time.localtime(time.time()).tm_mon
        CreationTime["day"] = time.localtime(time.time()).tm_mday
        CreationTime["hour"] = random.randint(7, 9)
        CreationTime["min"] = random.randint(0, 60)
        CreationTime["sec"] = random.randint(0, 60)
    elif flag == 3 or flag == 7:
        CreationTime["year"] = time.localtime(time.time()).tm_year
        CreationTime["mon"] = time.localtime(time.time()).tm_mon
        CreationTime["day"] = time.localtime(time.time()).tm_mday
        CreationTime["hour"] = random.randint(7, 12)
        CreationTime["min"] = random.randint(0, 60)
        CreationTime["sec"] = random.randint(0, 60)
    elif flag == 4:
        CreationTime["year"] = time.localtime(time.time()).tm_year
        CreationTime["mon"] = time.localtime(time.time()).tm_mon
        CreationTime["day"] = time.localtime(time.time()).tm_mday
        CreationTime["hour"] = random.randint(7, 15)
        CreationTime["min"] = random.randint(0, 60)
        CreationTime["sec"] = random.randint(0, 60)
    elif flag == 5:
        CreationTime["year"] = time.localtime(time.time()).tm_year
        CreationTime["mon"] = time.localtime(time.time()).tm_mon
        CreationTime["day"] = time.localtime(time.time()).tm_mday
        CreationTime["hour"] = random.randint(7, 17)
        CreationTime["min"] = random.randint(0, 60)
        CreationTime["sec"] = random.randint(0, 60)
    elif flag == 9:
        CreationTime["year"] = time.localtime(time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60).tm_year
        CreationTime["mon"] = time.localtime(time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60).tm_mon
        CreationTime["day"] = time.localtime(time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60).tm_mday
        CreationTime["hour"] = 6
        CreationTime["min"] = random.randint(20, 40)
        CreationTime["sec"] = random.randint(0, 60)

    return CreationTime

"""
:name: CalClosingTime
:brief: According to the flag to calculte the closing time
:param: flag -> int
:return: ClosingTime -> Dict ={"year","mon","day","hour","min","sec"}
"""
def CalClosingTime(flag: int) -> Dict:
    ClosingTime = {}
    if flag == 0 or flag == 6 or flag == 8:
        ClosingTime["year"] = time.localtime(time.time()).tm_year
        ClosingTime["mon"] = time.localtime(time.time()).tm_mon
        ClosingTime["day"] = time.localtime(time.time()).tm_mday
        ClosingTime["hour"] = random.randint(7, 10)
        ClosingTime["min"] = random.randint(0, 60)
        ClosingTime["sec"] = random.randint(0, 60)
    elif flag == 1:
        ClosingTime["year"] = time.localtime(time.time()).tm_year
        ClosingTime["mon"] = time.localtime(time.time()).tm_mon
        ClosingTime["day"] = time.localtime(time.time()).tm_mday
        ClosingTime["hour"] = random.randint(8, 10)
        ClosingTime["min"] = random.randint(0, 60)
        ClosingTime["sec"] = random.randint(0, 60)
    elif flag == 2:
        ClosingTime["year"] = time.localtime(time.time()).tm_year
        ClosingTime["mon"] = time.localtime(time.time()).tm_mon
        ClosingTime["day"] = time.localtime(time.time()).tm_mday
        ClosingTime["hour"] = random.randint(10, 12)
        ClosingTime["min"] = random.randint(0, 60)
        ClosingTime["sec"] = random.randint(0, 60)
    elif flag == 3 or flag == 7:
        ClosingTime["year"] = time.localtime(time.time()).tm_year
        ClosingTime["mon"] = time.localtime(time.time()).tm_mon
        ClosingTime["day"] = time.localtime(time.time()).tm_mday
        ClosingTime["hour"] = random.randint(13, 15)
        ClosingTime["min"] = random.randint(0, 60)
        ClosingTime["sec"] = random.randint(0, 60)
    elif flag == 4:
        ClosingTime["year"] = time.localtime(time.time()).tm_year
        ClosingTime["mon"] = time.localtime(time.time()).tm_mon
        ClosingTime["day"] = time.localtime(time.time()).tm_mday
        ClosingTime["hour"] = random.randint(16, 17)
        ClosingTime["min"] = random.randint(0, 60)
        ClosingTime["sec"] = random.randint(0, 60)
    elif flag == 5:
        ClosingTime["year"] = time.localtime(time.time()).tm_year
        ClosingTime["mon"] = time.localtime(time.time()).tm_mon
        ClosingTime["day"] = time.localtime(time.time()).tm_mday
        ClosingTime["hour"] = random.randint(18, 20)
        ClosingTime["min"] = random.randint(0, 60)
        ClosingTime["sec"] = random.randint(0, 60)
    elif flag == 9:
        ClosingTime["year"] = time.localtime(time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60).tm_year
        ClosingTime["mon"] = time.localtime(time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60).tm_mon
        ClosingTime["day"] = time.localtime(time.time() - time.localtime(time.time()).tm_wday * 24 * 60 * 60).tm_mday
        ClosingTime["hour"] = random.randint(7, 10)
        ClosingTime["min"] = random.randint(0, 60)
        ClosingTime["sec"] = random.randint(0, 60)

    return ClosingTime


def CalDays(flag: int, Value: Dict) -> float:
    if flag == 0:
        return 0.03
    elif flag == 1 or flag == 2 or flag == 3 or flag == 4:
        return 0.07
    elif flag == 5:
        return 0.11
    elif flag == 6:
        return 0.22
    elif flag == 7:
        return 0.16
    elif flag == 8:
        return 0.62
    elif flag == 9:
        return 4.62
    elif flag == 10:
        year_sec: int = (Value["EndTime"]["year"] - Value["StartTime"]["year"]) * 365 * 24 * 60 * 60
        mon_sec: int = (Value["EndTime"]["mon"] - Value["StartTime"]["mon"]) * 30 * 24 * 60 * 60
        day_sec: int = (Value["EndTime"]["day"] - Value["StartTime"]["day"]) * 24 * 60 * 60
        hour_sec: int = (Value["EndTime"]["hour"] - Value["StartTime"]["hour"]) * 60 * 60
        min_sec: int = (Value["EndTime"]["min"] - Value["StartTime"]["min"]) * 60
        sec_sec: int = Value["EndTime"]["sec"] - Value["StartTime"]["sec"]
        sec: float = year_sec + mon_sec + day_sec + hour_sec + min_sec + sec_sec
        DayValue: float = round(sec / 60 / 60 / 24, 2)
        return DayValue
