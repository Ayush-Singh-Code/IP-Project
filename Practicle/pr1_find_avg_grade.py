# Taking User input of there marks 

sub1 = float(input("Please enter the marks of Maths: "))
sub2 = float(input("Please enter the marks of Physics: "))
sub3 = float(input("Please enter the marks of Chemistry: "))
sub4 = float(input("Please enter the marks of English: "))
sub5 = float(input("Please enter the marks of IP: "))

# Finding Average
avg = (sub1+sub2+sub3+sub4+sub5)/5

# Printing Average
print("Your average is: ", avg)

# Deciding the Grade

if (avg>90):
    print("Grade: A")
elif (avg<90 and avg>=80):
    print("Grade: B")
elif (avg<80 and avg>=70):
    print("Grade: C")
elif (avg<70 and avg>=60):
    print("Grade: D")
elif (avg<60 and avg>=50):
    print("Grade: E")
else:
    print("Grade: F")
