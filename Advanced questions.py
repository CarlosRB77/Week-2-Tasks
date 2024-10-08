number = int(input("Input a number"))

while number > 0 : 
   loop_counter = number 
   while loop_counter > 0 :
      if loop_counter > 1:
        print (number , end=" ")
      else:
         print (number)
      loop_counter -= 1
   number -= 1