num,num1=map(int,input().split())
for i in range(num+1,num1):
  if i>1:
    for yy in range(2,i):
      if(i%yy==0):
        break
    else:
      print(i,end=" ")
