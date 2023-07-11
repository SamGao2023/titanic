name = input("What is your name?")
print("Thank you")
age = int(input("How old are you?"))
if age >= 5 and age < 11:
    school = "elementary"
    yesno = 1
elif age >= 11 and age <= 13:
    school = "middle"
    yesno = 1
elif age >= 14 and age <= 18:
    school = "high"
    yesno = 1
elif age >= 19 and age <= 24:
    school = "college"
    yesno = 2
else:
    yesno = 0

print("Thank you")
other = input("Is there anything else you like (e.g. fruit, people etc.)")
answer = input("Would you like me to write a self-introduction for you?")

if answer == "yes" and yesno == 1:
    print("Hi, my name is " + name + " and I am " + str(age) + " years old. I'm currently in " + school + " school. I also like " + other + ".")
elif answer == "yes" and yesno == 2:
    print("Hi, my name is " + name + " and I am " + str(age) + " years old. I'm currently in " + school + ". I also like " + other + ".")
elif answer == "yes" and yesno == 0:
    print("Hi, my name is " + name + " and I am " + str(age) + " years old. I also like " + other + ".")
else:
    print("Ok, bye")
