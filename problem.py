ages={
    "chetan":23,
    "modi":22,
    "jain":33
}
old=0 #here we can use None or 0
currnt=0
for name in ages:
    age=ages[name] #fatch the gae of name
    if age>currnt:
        old=name
        currnt=age
print(old)