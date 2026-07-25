#1 str=input("enter the username:")
# print(len(str))

#2 str="$my$name$is$dhairya$i$am$19$years$old$."
# print(str.count("$"))

#3 mrk=int(input("Enter the marks of a student:"))
# if(mrk>=90):
#     print("A")
# elif(mrk>=80 and mrk<90):
#     print("B")
# elif(mrk>=70 and mrk<80):
#     print("C")
# elif(mrk<70):
#     print("D")
# print("Grade of a student is:",mrk)

#4 num=int(input("Enter the number:"))
# if(num%2==0):
#     print("***Even***")
# else:
#     print("***Odd***")

#5 u=int(input("Enter the first number:"))
# n=int(input("Enter the second number:"))
# o=int(input("Enter the third number:"))
# if(u>n):
#     if(u>o):
#         print("***u is greatest***")
#     else:
#         print("***o is greatest***")
# else:
#     if(n>o):
#         print("***n is greatest***")
#     else:
#         print("***o is greatest***")

#6 x=int(input("Enter the number:"))
# if(x%7==0):
#     print("***Number is divisible by 7***")
# else:
#     print("***Number is not divisible by 7***")

# *** mid-level ***

#1   x=int(input("Enter the number:"))
# if(x%3==0 and x%5==0):
#     print("***Number is divisible by both.***")
# elif(x%3==0):
#     print("***Number is divisible by 3.***")
# elif(x%5==0):
#     print("***Number is divisble by 5.***")
# else:
#     print("***Number is not divisible by both.***")

#2 t_cls=int(input("Enter the total classes:"))
# a_cls=int(input("Enter the attended classes:"))
# at_per= (a_cls/t_cls)*100
# print(f"The attendence is:{at_per}%.")
# if(at_per>=75):
#     print("***Eligible to give the exam.***")
# else:
#     print("***Not eligible to give the exam.***")

#3 units=float(input("Enter the number of units consumed:  "))
# if(units<=100):
#     bill=units*5
#     print(f"Total bill is:{bill} ruppees")
# else:
#     bill=(100*5)+((units-100)*8)
#     print(f"Total bill is:{bill} ruppees")

# print("Thanks for paying the bill")

#for a leap year:- should we divisible by 400 and 4 and not divisible by 100 

#4 psd=input("enter the password:")
# p_len=len(psd)
# if(p_len<6):
#     print("weak password.")
# elif(p_len>=6 and p_len<10):
#     print("medium password.")
# else:
#     print("strong password.")

#5 yr=int(input("enter the year:"))
# if(yr%400==0 or(yr%100!=0 and yr%4==0)):
#    print("leap year")
# else:
#    print("not a leap year")

# ***mid-hard***

#for a tringle checking:- sum of any two sides must be greayer than the third side.

#6 a=int(input("enter the first side of triangle:"))
# b=int(input("enter the second side of triangle:"))
# c=int(input("enter the third side of a triangle:"))
# if((a+b)>c and (b+c)>a and (c+a)>b):
#     print("trinagle will form")
# else:
#     print("will not form")
    
#7 a=int(input("enter the first side of triangle:"))
# b=int(input("enter the second side of triangle:"))
# c=int(input("enter the third side of a triangle:"))
# if(a>b):
#     if(a>c):
#         print("a is the greatest.")
#     else:
#         print("c is the greatest.")
# elif(b>c):
#     if(b>a):
#         print("b is the greatest.")
#     else:
#         print("a is the greatest.")
# elif(c>a and c>b):
#     print("c is the greatest.")
# else:
#     print("none of the number is greatest")

#8 u="dspark"
# p=1234567890
# u_n=input("enter the username:")
# psd=int(input("enter the password:"))
# if(u_n==u and psd==p):
#     print("login successfull")
# elif(u_n!=u and psd==p):
#     print("username is incorrect")
# elif(u_n==u and psd!=p):
#     print("password is not correct")
# else:
#     print("both username and password is wrong")

#9 w=float(input("enter your weight:"))
# h=float(input("enter your height:"))
# bmi=(w/(h*h))
# print(f"BMI={bmi}")
# if(bmi<18.5):
#     print("underweight")
# elif(bmi>=18.5 and bmi<24.9):
#     print("normal weight")
# elif(bmi>=24.9 and bmi<29.9):
#     print("overweight")
# elif(bmi>=30):
#     print("obese")
# else:
#     print("invalid")

#10 x=int(input("enter the number:"))
# if(x>=0 and x%2==0):
#     print("Even")
# elif(x>=0 and x%2!=0):
#     print("odd")
# elif(x%2==0):
#     print("-ve even")
# elif(x%2!=0):
#     print("-ve odd")
# else:
#     print("none of the categorie")

#***hard-level***

#11 c="rock"
# i=input("enter the input:")
# if(i=="rock" and c=="rock"):
#     print("Rematch")
# elif(i=="sicsor" and c=="rock"):
#     print("computer won.")
# elif(i=="paper" and c=="rock"):
#     print("user won.")
# else:
#     print("not the part of game")

#12 a=int(input("enter the first number: "))
# op=input("enter the operator:")
# b=int(input("enter the second number:"))
# if(op=="+"):
#     r=a+b
#     print(f"result:{r}")
# elif(op=="-"):
#     r=a-b
#     print(f"result:{r}")
# elif(op=="*"):
#     r=a*b
#     print(f"result:{r}")
# elif(op=="/"):
#     r=a/b
#     print(f"reslut:{r}")
# elif(op=="%"):
#     r=a%b
#     print(f"reslut:{r}")
# elif(op=="**"):
#     r=a**b
#     print(f"reslut:{r}")
# else:
#     print("invalid")

#13 age=int(input("enter your age:"))
# c="child"
# cp=100
# a="adult"
# ap=200
# s="senior"
# sp=120
# if(age<12):
#     print(f"category:{c}\n",f"ticket price is:{cp}ruppees" )
# elif(age>=12 and age<=59):
#     print(f"category is:{a}\n ",f"ticket price is:{ap}ruppees")
# else:
#     print(f"category is:{s}\n",f"ticket price is:{sp}ruppees")

#14 bal=50000
# cb="check balance"
# dp="deposite"
# wd="withdraw"
# ask=input("what do u want to do:")
# if(ask==cb):
#     print(f"the balance is:{bal}ruppees")
# elif(ask==dp):
#     amt=int(input("enter the amount to be deposite:"))
#     t_amt=bal+amt
#     print(f"the balance is:{t_amt}ruppees")
# elif(ask==wd):
#     amt=int(input("enter the amount you want to withdraw:"))
#     t_amt=bal-amt
#     print(f"the balance is:{t_amt}ruppees ")
# else:
#     print("invalid")          