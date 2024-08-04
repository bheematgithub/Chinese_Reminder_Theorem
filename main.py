try:
  t=int(input("Total no of elements = "))
  n,x,N=[],[],1
  for i in range(t):
    n.append(int(input(f"\nn{i+1} = ")))
    x.append(int(input(f"x{i+1} = ")))
    N*=n[i]
except :
  print("Enter only Intergers!")
  exit()

a=[N//i for i in n]

s,ss="",""
alp=[]
for i in range(t):
  s+=f"\na{i+1} = {N}/{n[i]} = {a[i]}"
  for j in range(1,n[i]):
    if (j*a[i])%n[i]==1:
      alp.append(j)
      ss+=f"\nalpha{i+1} => {j} * {a[i]} = 1 mod {n[i]}"
      break
  else:
    print(f"\nNo modular inverse found for modulus {n[i]}")
    exit()

print(s)
print(ss)

s,ss,sum="","",0
for i in range(t):
  if i == 0:
      s += f"x = ({x[i]}*{a[i]}*{alp[i]})"
      ss += f"x = ({x[i]*a[i]*alp[i]})"
  elif i == t - 1:
      s += f" + ({x[i]}*{a[i]}*{alp[i]}) mod {N}"
      ss += f" + ({x[i]*a[i]*alp[i]}) mod {N}"
  else:
      s += f" + {x[i]}*{a[i]}*{alp[i]}"
      ss += f" + {x[i]*a[i]*alp[i]}"

  sum += x[i] * a[i] * alp[i]
  
print("\n",s,"\n",ss,
      "\n x =",sum,"mod",N,
      "\n x =",sum%N)
exit()
