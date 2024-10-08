number = int(input("Input a number "))

for x in range (1 , number + 1):
    loop_counter = x 
    while loop_counter > 0 :
      if loop_counter > 1:
        print (x , end=" ")
      else:
         print (x)
      loop_counter -= 1
    x += 1