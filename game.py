import random
winning_number = random.randint(1,100)
i = 1
while True:
   num = int(input("enter any number"))

   if num == winning_number:
      print("you win")
      print(i)
      break
   else:
         if  num > winning_number:
              print("too high")

         else:
              print("too low")
   i += 1
   continue
