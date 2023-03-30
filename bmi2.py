
name = input("enter your name: ")                   #Ask the user for name
weight = int(input("enter your weight in kgs"))     #ask height
height = float(input("enter your height in feet"))  #ask weight
height_in_meters = height*0.3                       #convert height to meters
bmi = weight/(height_in_meters * height_in_meters)  #print bmi

print(f"Hello {name} your bmi is {round(bmi,2)}")
