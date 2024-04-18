:<<!
:file: pack.sh
:brief: To pack this project
:version: 2.0
:author: SWfeiyu
:date: 2024.4.18
!

pyinstaller -F main.py -n AFLtool

mv ./dist/AFLtool* ./
rm -rf build dist AFLtool.spec

echo "The executable program has been successfully built, thank you for using it."

