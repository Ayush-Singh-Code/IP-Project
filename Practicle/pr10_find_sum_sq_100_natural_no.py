# To find the sum of squares of the first 100 natural numbers.


#uncommit below code to find sum of 100 natural no
#number = 100

# using formula from sequence and series 
#sum_sq  = number*(number+1)*(2*number+1)/6

#print(sum_sq)

# ------------------------------------------------------------------------------ # 

# Modified code for more efficency 
print("To find the sum of squares of the first n natural numbers.")

number = int(input("Enter the number you want sum of: "))

# Formula from sequence and series
# sigma n^2 = n(n+1)(2n+1)/6

sumOfNumber = number*(number+1)*(2*number+1)/6
print(sumOfNumber)