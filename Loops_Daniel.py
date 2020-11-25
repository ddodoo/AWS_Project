#AWS_Restart
#Ghanaian Names Days Of The Week
#Daniel Nii Amu Dodoo

#Populating the days of the week in an array

daysOfWeek = []

prefixes = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

while len(daysOfWeek) < 7:
    for prefix in prefixes:
        day = input('Enter the ' + prefix + " day of the week:")
        daysOfWeek.append(day.capitalize())
        print(daysOfWeek)

        if  daysOfWeek.count(day) > 1:
            daysOfWeek.pop()
            day = input ('Enter the' + prefix + " day of the week again:")
            daysOfWeek.append(day.capitalize())
            print(daysOfWeek)

            
#User inputs sex and day born
sex_Male_Female = input("Enter Your Sex, Male or Female:")
day_Born = input("Enter the day of the week you were born:")


#Compares users inputs to days 
if sex_Male_Female == "Male" and day_Born == "Monday":
        print("Kwadwo")
elif sex_Male_Female == "Female" and day_Born == "Monday":
        print("Ajua")

if sex_Male_Female == "Male" and day_Born == "Tuesday":
    print("Kwabena")

elif sex_Male_Female == "Female" and day_Born == "Tuesday":
    print("Abena")

if sex_Male_Female == "Male" and day_Born == "Wednesday":
    print("Kwaku")

elif sex_Male_Female == "Female" and day_Born == "Wednesday":
    print("Akua")

if sex_Male_Female == "Male" and day_Born == "Thursday":
    print("Yaw")

elif sex_Male_Female == "Female" and day_Born == "Thursday":
    print("Yaa")

if sex_Male_Female == "Male" and day_Born == "Friday":
    print("Kofi")

elif sex_Male_Female == "Female" and day_Born == "Friday":
    print("Afia")

if sex_Male_Female == "Male" and day_Born == "Saturday":
    print("Kwame")

elif sex_Male_Female == "Female" and day_Born == "Saturday":
    print("Ama")

if sex_Male_Female == "Male" and day_Born == "Sunday":
    print("Kwesi")

elif sex_Male_Female == "Female" and day_Born == "Sunday":
    print("Esi")












