num=int(input())
pp=0
hh=num
while hh>0:
  digit = hh%10
  pp += digit **3
  hh //=10
if num==pp:
  print("yes")
else:
  print("no")
