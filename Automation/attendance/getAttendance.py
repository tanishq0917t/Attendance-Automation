import pathlib
import sys
import subprocess
class attd:
    def __init__(self):
        self.present=0
        self.absent=0
    def countAttendance(self,deptCode,employeeCode,month,folder):
        folder=pathlib.Path(folder)
        for entry in folder.iterdir():
            if entry.is_file():
                #print(entry.name)
                with open(entry,"rb") as dataFile:
                    while True:
                        a=dataFile.readline()
                        if len(a)==0: break
                        a=a.decode(encoding="utf-8")
                        a=a.strip()
                        a=eval(a)
                        if a[0]==employeeCode:
                            if a[1]=='P': self.present+=1
                            else: self.absent+=1
        print(self.present)
        print(self.absent)

deptCode=int(input())
employeeCode=int(input())
month=input().upper()
a=attd()
folder="C:\\work\\python\\pyapps\\autoeg1\\att\\dept"+str(deptCode)+"\\"+month
#print(folder)
a.countAttendance(deptCode,employeeCode,month,folder)
