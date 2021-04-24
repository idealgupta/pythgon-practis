name = input("enter the student name : ")
marks=int(input("enter the marks : "))
if marks<35:
    print(name,"is fail GRADE : F")
elif marks>=35 and marks<=40:
    print(name ,"pass GRADE : D")
elif marks>=41 and marks<50:
    print(name,"pass GRADE : C ")
elif marks>=51 and marks<60:
    print(name,"pass GRADE : B")
elif marks>=61 and marks<70:
    print(name,"pass GRADE : B+")
elif marks>=71 and marks<80:
    print(name,"pass GRADE : A")
else:
    print("GRADE :A+")