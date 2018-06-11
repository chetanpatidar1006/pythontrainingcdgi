def car(speed):
    if speed>=200:
        print("to fast")
    elif speed>100:
        print("fast")
    elif speed>70:
        print("not bad")
    else:
        print("very good")

c=int(input("enter the speed20"))
car(c)