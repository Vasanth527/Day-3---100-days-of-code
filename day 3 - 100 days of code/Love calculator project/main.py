# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


l1 = name1.lower()
l2 = name2.lower()
T = l1.count('t') + l2.count('t')
R = l1.count('r') + l2.count('r')
U = l1.count('u') + l2.count('u')
E = l1.count('e') + l2.count('e')
TRUE = T + R + U + E
L = l1.count('l') + l2.count('l')
O = l1.count('o') + l2.count('o')
V = l1.count('v') + l2.count('v')
E = l1.count('e') + l2.count('e')
LOVE = L + O + V + E 
TRUE_LOVE = str(TRUE)+ str (LOVE)
if int (TRUE_LOVE) < 10 or int (TRUE_LOVE) > 90 :
    print(f"Your score is {TRUE_LOVE}, you go together like coke and mentos.")
elif int (TRUE_LOVE) > 40 and int (TRUE_LOVE) < 50 :
    print(f"Your score is {TRUE_LOVE}, you are alright together.")
else :
    print(f"Your score is {TRUE_LOVE}.")    
