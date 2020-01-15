parrot="Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[3]+parrot[4]+ " "+parrot[3]+parrot[6]+parrot[8])
print(parrot[-1])
print(parrot[-14])
print(parrot[3-14])
print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
number="9,223;372:036 854,775;807"
seperators=number[1::4];
print(number[1::4]) #from index 1 with jump of 4
values="".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
    




