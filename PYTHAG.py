from math import *
while True:
  cho=int(input("mode:\n> "))
  a = None
  b = None
  if str(cho) != str(4):
    a=eval(input("What is your A value?\n>  "))
    b=eval(input("What is your B value?\n> "))
  if str(cho)==str(1):
    c=sqrt(float(a)**2+float(b)**2)
    print("Your C value is "+ str(c))
    parts = int(input("Do you want to see the parts?\n> "))
    if str(parts )== str(1):
      print("\nA**2:", a ** 2, "\nB**2:", b ** 2, "\nC**2:", c ** 2, "\nRoot:",a**2+b**2)
  elif str(cho)==str(2):
    c=eval(input("What is your C value?\n> "))
    ab=float(a)**2+float(b)**2
    cc=float(c)**2
    if str(ab)==str(cc):
      print("Your triangle is classifyed as a RIGHT triangle.")
    elif str(cc)>str(ab):
      print("Your triangle is classifyed as a OBTUSE triangle.")
    else:
      print("Your triangle is classifyed as a ACUTE triangle.")
    parts = int(input("Do you want to see the parts?\n> "))
    if str(parts )== str(1):
      print("\nA**2:", a ** 2, "\nB**2:", b ** 2,"\nA**2+B**2:", ab,"\nC**2:", c ** 2, "\nRoot:",float(a) ** 2 + float(b) ** 2)
  elif str(cho)==str(3):
    t=float(input("How many degrees: "))
    c=a**2+b**2-2*a*b*cos(radians(t))
    c=sqrt(c)
    print("Your C value is " + str(c))
  elif str(cho) == str(4):
    a = eval(input("What is the measure of your leg?\n> "))
    c = eval(input("What is the measure of your hypotonuse?\n> "))
    cc = c**2
    aa = a**2
    bb = cc-aa
    b = sqrt(bb)
    print("The measure of the second leg is:",b)
    parts = int(input("Do you want to see the parts?\n> "))
    if str(parts )== str(1):
      print("\nA**2:", aa, "\nB**2:", bb, "\nC**2:", cc,"\nC**2 - A**2:",bb)
