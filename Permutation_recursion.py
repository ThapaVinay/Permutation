tt = 0
def fun(a,b,n):
    t=[]
    global tt
    if n>=0:
        for i in range(n):                   
                tt+=1
                fun(a,b,n-1)
                temp=b[n]
                b[n]=b[n-1]
                b[n-1]=temp
                temp=1
                x=0
                for i in range(len(b)):
                    x+=temp*b[i]
                    temp=temp*10
                count=0
                for i in a:
                    count=0
                    if x==i:
                        count+=1
                        break
                if count==0: 
                    a.append(x)
                t=b.copy()
        fun(a,t,n-1)



a=int(input("Enter a Number (Non-Negitive Number) -:"))
b=[]
c=[]
i=a
count=0
if a<0:
    print("Error Occured - Negitve Number Found.")
    exit(0)


# dividing the given number into different numbers like [123] -> [1,2,3]
while(i!=0):
    b.append(i%10)
    i//=10
c.append(a)

# passing a new list, and given array
fun(c,b,len(b)-1)
print("\n",c)
print(tt)
