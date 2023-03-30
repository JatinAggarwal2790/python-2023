
name = input("enter your name: ")                   #Ask the user for name
weight = int(input("enter your weight in kgs"))     #ask height
height = float(input("enter your height in feet"))  #ask weight
height_in_meters = height*0.3                       #convert height to meters
bmi = weight/(height_in_meters * height_in_meters)  #print bmi

print(f"Hello {name} your bmi is {round(bmi,2)}")

if bmi < 18:
    print("Under weight")

if bmi < 18:
    print("Under weight")
else:
    print("You are not Under weight")


if bmi <= 18.5:
    print("Under weight")
elif bmi >18.5 and bmi <= 24.9:
    print("Normal")
elif bmi >24.9 and bmi <= 29.9:
    print("over weight")
else:
    print("obese")
print("bye")
