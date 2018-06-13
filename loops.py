#for loop
for food in [1, 4, 7, 9]:
  print (food) 

  for food in range(9):
  print (food**7) 

#while loop
  counter = 1
  while counter <=9:
  	print("Hello, world")
  	counter = counter +1

  
#if else statement
score = 100
		if score >= 90:
   print('A')
else:
   if score >=80:
      print('B')
   else:
      if score >= 70:
         print('C')
      else:
         if score >= 60:
            print('D')
         else:
            print('y')

#elif statement
score = 50
           if score >= 90:
   print('A')
elif score >=80:
   print('B')
elif score >= 70:
   print('C')
elif score >= 60:
   print('D')
else:
   print('F')