num,num1=map(int,input().split())
for i in range(num+1,num1):
  sum=0
  num2=i
  while(num2>0):
    x=num2%10
    num2=num2//10
    y=x**3
    sum=sum+y
  if(i==sum):
    print(sum,end=' ')
