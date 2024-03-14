from typing import Dict


def BuildStr(Value: Dict) -> Dict:
    ValueStr = {
        "Name": Value["Name"],
        "StudentID": Value["StudentID"],
        "AcademicYear": "学年：" + str(Value["AcademicYear"]) + "-" + str(Value["AcademicYear"] + 1),
        "Class": "班级：" + Value["Class"],
        "Type": "请假类型：因私-病假",
        "Days": "请假天数：" + str(Value["Days"]),
        "Apply": "是否补假申请：是",
        "State": "状态："
    }
    if Value["Semester"] == 1:
        ValueStr["Semester"] = "学期：第一学期"
    elif Value["Semester"] == 2:
        ValueStr["Semester"] = "学期：第二学期"
    if Value["Gender"] == 'm':
        ValueStr["Gender"] = "性别：男性"
    elif Value["Gender"] == 'w':
        ValueStr["Gender"] = "性别：女性"
    ValueStr["StartTime"] = (
        "请假开始时间：{0}-{1}-{2} {3}:{4}:{5}".format(
            str(Value["StartTime"]["year"]),
            str(Value["StartTime"]["mon"]).rjust(2, '0'),
            str(Value["StartTime"]["day"]).rjust(2, '0'),
            str(Value["StartTime"]["hour"]).rjust(2, '0'),
            str(Value["StartTime"]["min"]).rjust(2, '0'),
            str(Value["StartTime"]["sec"]).rjust(2, '0')
        )
    )
    ValueStr["EndTime"] = (
        "请假结束时间：{0}-{1}-{2} {3}:{4}:{5}".format(
            str(Value["EndTime"]["year"]),
            str(Value["EndTime"]["mon"]).rjust(2, '0'),
            str(Value["EndTime"]["day"]).rjust(2, '0'),
            str(Value["EndTime"]["hour"]).rjust(2, '0'),
            str(Value["EndTime"]["min"]).rjust(2, '0'),
            str(Value["EndTime"]["sec"]).rjust(2, '0')
        )
    )
    ValueStr["CreationTime"] = (
        "创建时间：{0}-{1}-{2} {3}:{4}:{5}".format(
            str(Value["CreationTime"]["year"]),
            str(Value["CreationTime"]["mon"]).rjust(2, '0'),
            str(Value["CreationTime"]["day"]).rjust(2, '0'),
            str(Value["CreationTime"]["hour"]).rjust(2, '0'),
            str(Value["CreationTime"]["min"]).rjust(2, '0'),
            str(Value["CreationTime"]["sec"]).rjust(2, '0')
        )
    )
    ValueStr["ClosingTime"] = (
        "创建时间：{0}-{1}-{2} {3}:{4}:{5}".format(
            str(Value["ClosingTime"]["year"]),
            str(Value["ClosingTime"]["mon"]).rjust(2, '0'),
            str(Value["ClosingTime"]["day"]).rjust(2, '0'),
            str(Value["ClosingTime"]["hour"]).rjust(2, '0'),
            str(Value["ClosingTime"]["min"]).rjust(2, '0'),
            str(Value["ClosingTime"]["sec"]).rjust(2, '0')
        )
    )

    return ValueStr

