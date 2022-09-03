def fact(a):
    sum = 1
    for i in range(1,a+1):
        sum = sum *i
    return sum


import random
a=int(input("Enter a Number (Non-Negitive Number) -:"))
b=[]
c=[]
d=[]
i=a
count=0
if a<0:
    print("Error Occured - Negitve Number Found.")
    exit(0)


# we are finding the total possible combinations that are possible so that we can terminate the loop
while(i!=0):
    b.append(i%10)
    i//=10
sum = fact(len(b))      
t = []

# if numbers are same then divide them to get possible combinations
for i in b:
    z = b.count(i)
    if(z not in t):
        sum = sum//fact(z)     
    t.append(z)

    
while(len(c) != sum):
    x = []
    while(1):
        d  = []
        while(1):
            v = b[random.randint(0,len(b)-1)]  #finding a random number
            if (d.count(v) < b.count(v)):   # checking if the length of the number is less or not
                d.append(v)
            if(len(d) == len(b)):   # if length is equal then the number is complete
                break
        temp=1
        x=0
        for i in range(len(d)):  # joining the numbers to form a single number [1,2,3] -> [321]
            x+=temp*d[i]
            temp=temp*10
        if(x not in c): 
            break
    c.append(x)  
print(c)
