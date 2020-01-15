list=""
for i in range(2000,3201):
    if((i%7==0)and(i%5!=0)):
        list+=(str(i)+", ")

print(list[0:len(list)-2])
#2
str=input("please enter a string\n")
for i in range(len(str)-1):
    if(i%2==0):
        print(str[i])
#3 reverse

str2=input("enter strin to print in reverse\n")
print(str2[len(str2)-1::-1])


