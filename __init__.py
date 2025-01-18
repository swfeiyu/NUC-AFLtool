from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.params import ArgPlainText
from . import cal
from . import strbuild
from . import draw


alftool = on_command("假条", rule=to_me(), priority=10, block=True)
@alftool.got("Name",prompt="请输入你的姓名")
@alftool.got("StudentID",prompt="请输入你的学号")
@alftool.got("Class",prompt="请输入你的班号")
@alftool.got("Gender",prompt="请输入你的性别(男/女)")
@alftool.got("Flag",prompt="请输入请假时间(回复序号)\n0.早读时间\n1.上午第一节课\n2.上午第二节课\n3.下午第一节课\n4.下午第二节课\n5.晚上上课\n6.整个上午\n7.整个下午\n8.整天\n9.整周")
@alftool.handle()
async def handle_function(Name: str = ArgPlainText(), StudentID: str = ArgPlainText(), Class: str = ArgPlainText(), Gender: str = ArgPlainText(), Flag: str = ArgPlainText()):
    Flag=int(Flag)
    Value = {
        "Name": Name,
        "StudentID": StudentID,
        "Class": Class,
        "Gender": Gender,
        "AcademicYear": cal.CalAcademicYear(),
        "Semester": cal.CalsSemester(),
        "StartTime": cal.CalStartTime(Flag),
        "EndTime": cal.CalEndTime(Flag),
        "CreationTime": cal.CalCreationTime(Flag),
        "ClosingTime": cal.CalClosingTime(Flag)
    }
    Value["Days"] = cal.CalDays(Flag,Value)
    draw.Draw(strbuild.BuildStr(Value))

    img = MessageSegment.image("file:///root/nb/awesome_bot/plugins/NUC-AFLtool/output/note.jpg")

    await alftool.finish(img)
