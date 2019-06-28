num=int(input())
pp=0
hh=z
while hh>0:
  digit = hh%10
  pp += digit **3
  hh //=10
if z==pp:
  print("yes")
else:
  print("no")
