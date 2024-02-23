def menor(a,b,c,d):
  if a > d and b > d and c > d:
    print(d,"d")
  elif a > c and b > c:
    print(c,"c")
  elif a > b:
    print(b,"b")
  else: 
    print(a,"a")

menor(1, 2, 3, 4)
menor(2, 3, 4, 1)
menor(3, 4, 1, 2)
menor(4, 1, 2, 3)