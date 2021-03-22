import pathlib
import sys
import collections as coll
with open("C:\\work\\python\\pyapps\\autoeg1\\emp\\emp.data","rb") as dataFile:
    flag=0
    while True:
        a=dataFile.readline()
        if len(a)==0: break
        a=a.decode(encoding="utf-8")
        a=a.strip()
        a=eval(a)
        if a[0]==int(sys.argv[1]):
            flag=1
            print(a[2])
            break
    if not flag: print(0)
