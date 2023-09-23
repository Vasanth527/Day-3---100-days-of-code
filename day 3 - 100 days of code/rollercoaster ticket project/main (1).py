print("welcome to roller coaster!")
height = int(input("what is your height in cm?"))

if height >= 120 :
  print("you can ride the rollercoaster!")
  age = int(input("what is your age?"))
  if age <12:
    bill = 5
    print("child tickets are $5.")
  elif age <=18:
    bill = 7
    print("youth tickets are %7.")
  elif age>=45 and age <=55:
    bill = 0
    print("your tickets are $0")  
  elif age > 18:
    bill = 12
    print("adult tickets are $12.")
  

  want_photo = input("Do you want a photo taken? Y or N")
  if want_photo == "Y":
    bill += 3
  print (f"your final bill is {bill}")

else:
  print ("sorry, you have to grow taller before you can ride.")
  
