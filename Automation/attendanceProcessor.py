import pathlib
import sys
import subprocess
employee_id=input("Enter employee id: ")
with open("temp.data","w+") as temp:
    pth="c:\\work\\python\\pyapps\\autoeg1\\emp\\getDeptCode.py"
    subprocess.run(["py",pth,employee_id],stdout=temp)
with open("temp.data","rb") as temp:
    a=temp.readline()
    a=a.decode(encoding="utf-8")
    if int(a)==0:
        print("Invalid Employee Id")
        sys.exit(0)
    else:
        month=input("Enter month:")
        with open("c:\\work\\python\\pyapps\\autoeg1\\att\\input.data","w+") as inputFile:
            inputFile.write(a.strip()+"\n")
            inputFile.write(employee_id+"\n")
            inputFile.write(month.upper()+"\n")
        pth="c:\\work\\python\\pyapps\\autoeg1\\att\\getAttd.py"
        with open("c:\\work\\python\\pyapps\\autoeg1\\att\\input.data","rb") as inputFile:
            with open("finalOutput.data","w+") as fout:
                subprocess.run(["py",pth,employee_id],stdout=fout,stdin=inputFile)
with open("c:\\work\\python\\pyapps\\autoeg1\\finalOutput.data","rb") as fout:
    print("Present Days:",(fout.readline().decode(encoding="utf-8")).strip())
    print("Absent Days:",(fout.readline().decode(encoding="utf-8")))
