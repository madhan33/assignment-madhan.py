#python program to print positive numbers in a list

numlist = []

x=0


number =int(input("enter the total number of list elements: "))
for i in range(1,number+1):
    value =int(input("enter the value of %d element: " %i))
    numlist.append(value)



print("\npositive numbers in this list are: ")
while(x < number):
    if(numlist[x] >= 0):
        print(numlist[x],end =' ')
    x = x+1    
