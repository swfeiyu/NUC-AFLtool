from typing import Dict
from PIL import Image, ImageDraw, ImageFont


def Draw(ValueStr: Dict):
    ZhLFont = ImageFont.truetype("font/regular.ttf", 50)
    ZhSFont = ImageFont.truetype("font/regular.ttf", 40)
    im = Image.open("img/test.jpg")
    imd = ImageDraw.Draw(im)

    imd.text((92, 789), ValueStr["Name"], font=ZhLFont, fill=(17, 17, 17))
    imd.text((92 + 50 * len(ValueStr["Name"]) + 46, 801), ValueStr["StudentID"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 900), ValueStr["AcademicYear"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 960), ValueStr["Semester"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1020), ValueStr["Class"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1080), ValueStr["Gender"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1140), ValueStr["Type"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1200), ValueStr["Days"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1260), ValueStr["Apply"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1320), ValueStr["StartTime"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1380), ValueStr["EndTime"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1440), ValueStr["CreationTime"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1500), ValueStr["ClosingTime"], font=ZhSFont, fill=(102, 102, 102))
    imd.text((90, 1560), ValueStr["State"], font=ZhSFont, fill=(102, 102, 102))

    im.save("output/note.jpg")
    print("Please view your application in the output folder.Thank you for using!")
