no1=10
no2=20
if(no1<no2):
    sum=no1+no2
    print(sum)
elif(no1>5):
    sub=no1-no2
    print(sub)
else:
    print("hello")


#largest of 3 numbers

no1=int(input("no1="))
no2=int(input("no2="))
no3=int(input("no3="))
if(no1>no2 ) and (no1>no3):
    largest=no1
elif(no2>no1) and (no2>no3):
    largest=no2
else:
    largest=no3
print("largest=",largest)

#turns 100 years

name=input("name=")
age=int(input("age="))
personAge=(100-age)+2021
print("the user will in year",personAge,"turn 100 years old")
