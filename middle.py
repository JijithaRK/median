n=int(input())
a=list(map(int,input().split()))
sum1=0
for i in range(0,n):
    sum1=sum1+a[i]
print(sum1//n)
    
