travelling=(input("are you going for travelling yes or no"))
while travelling=="yes":
    num=int(input("enter the no of people travelling"))
    for num in range(1, num+1):
        name= input("enter the detail \n name")
        age = input("age")
        sex=input("MALE OR FEMALE")
        print("details are:\n",name )
        print(age)
        print(sex)
    print("thank you")
    travelling=input("are you travelling or not")
print("pls come back")