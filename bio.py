name = input('Your name: ')
born = input('Your birth date: ')
age = input('Your age: ')
gender = input('Give gender: ')
qualification = input('Your qualification: ')
nationality = input('Your nationality: ')
religion = input('Your religion: ')
male = "male"
female = "female"

print("")

print("8888888 8888888 8    8  88    888888  88    8  8888888")
print("8          8    8    8  8 8   8       8 8   8     8   ")
print("8888888    8    8    8  8  8  8888    8  8  8     8   ")
print("      8    8    8    8  8  8  8       8   8 8     8   ")
print("8888888    8    888888  888   888888  8    88     8   ")

print("")

print("Student's name is " + name)

if gender == male:
    print("He was born on " + born)
elif gender == female:
    print("She was born on " + born)

if gender == male:
    print("He is " + age + " years old")
elif gender == female:
    print("She is " + age + " years old")
    
if gender == male:
    print("His qualification is " + qualification)
elif gender == female:
    print("Her qualification is " + qualification)

if gender == male:
    print("He is " + nationality)
elif gender == female:
    print("She is " + nationality)

if gender == male:
    print("His religion is " + religion)
elif gender == female:
    print("Her religion is " + religion)

    