# To calculate Simple and Compound interest

# provide option to chosse between simple and compound intrest

print('''Choose what you want to do:\n
         1. Simple intrest\n
         2. Compound intrest\n
         Only enter 1 or 2 ''')
print("-----------------------------------------------------------------")


# defining funvtion for simple and compound intrest 

def simpleIntrest():
    print("Selected Simple Intrest")
    principle = float(input("Enter Principle amount: "))
    rate = float(input("Enter rate of intrest: "))
    tenure = float(input("Enter Tenure(in year): "))
    resultSI = (principle * rate * tenure)/100
    print("Simple Intrest: ", resultSI) 

def compoundIntrest():
    print("Selected Compound Intrest")
    principle = float(input("Enter Principle amount: "))
    rate = float(input("Enter rate of intrest: "))
    tenure = float(input("Enter Tenure(in years): "))
    resultCI = (principle*(1+rate/100)**tenure)
    print("Compound Intrest: ", resultCI) 



selected_option = input("   Your Selection: ")
if (selected_option == "1"):
    simpleIntrest()

elif (selected_option == "2"):
    compoundIntrest()
else:
    print(''' ERRROR!
    PLEASE SELECT FROM 1 OR 2
    ''')

