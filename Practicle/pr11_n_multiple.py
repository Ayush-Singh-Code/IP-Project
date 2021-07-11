# To find n multiple of a number

chosseNum = int(input("Enter the number for which you want the multiple: "))

nMultiple = int(input("Enter the number till where you want the multiple: "))

# function for finding multiple 
def multiple():
   count = 0
   while(count < nMultiple):
       count = count + 1
       print(chosseNum * count)
multiple()
