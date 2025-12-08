Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
While loops  
#Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
#While loops  
# for loops = execute a block of code a fixed number of time
# you can iterate overa range, string, sequnce, etc...

for x in reversed(range(1, 11,2)):
    print(x)
    print("happy new year")

credit_card = "1243-2345-9834-3458"
for x in range(1, 21):
    if x ==13:
        continue
    else:
        print(x)    



# while loop = execute some code while some conditions remains true
name = input("enter your name:")

if name == "":
    print("you did not enter your name")
    name = input("enter your name:")
print(f"hello {name}")
while name == "":
    print("You did not enter your name")
    while age < 0:
        print("Age can not be negative")
        age = int(input("enter your age:"))

print(f"you are {age} years old")
