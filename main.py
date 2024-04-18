"""
:file: main.py
:brief: To write the main logic of this tool
:version: 2.0
:author: SWfeiyu
:date: 2024.4.18
"""

from getdata import *
from strbuild import *
from draw import *

if __name__ == '__main__':
    Draw(BuildStr(GetData()))

