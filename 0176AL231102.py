#Name-Rounak Yadav
#Enrollment-0176AL231102
#Batch-5
#Batch time-10:30am to 12:10pm

print("**Basic If-Else Problems**")

print("Q-1")
n=int(input("Enter a number: "))
if n>0:
  print("your number is positive")
elif n<0:
  print("your number is negative")
else:
  print("its zero")

print("Q-2")
#using input value taken in q-1
if n%2==0:
  print("your number is even")
else:
  print("your number is odd")

print("Q-3")
year=int(input("Enter the year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
  print(year," is leap year")
else:
  print(year," is not leap year")

print("Q-4")
nu1=int(input("Enter first no: "))
nu2=int(input("Enter second no: "))
if n1>=n2:
  print(n1," is greater")
else:
  print(n2," is greater")

print("Q-5")
age=int(input("Enter age: "))
if age>=18:
  print("You are eligible to vote")
else:
  print("You are not eligible to vote")

print("Q-6")
char=input("Enter a character: ").lower()
vowels=["a","e","i","o","u"]
if char in vowels:
  print(ch," is a vowel")
else:
  print(ch," is a consonant")

print("Q-7")
n1 = int(input("Enter a no: ")) 
if n1%5==0:
  print(n1," is divisible by 5")
else:
  print(n1," is not divisible by 5")

print("Q-8")
n2=int(input("Enter a no: "))
if n2<10:
  print(n2," is a single digit no")
elif n2<100 and n2>9:
  print(n2," is a two-digit no")
else:
  print(n2," has more than 2 digits")

print("Q-9")
mark=int(input("Enter marks: "))
if mark>=40:
  print("You passed")
else:
  print("You failed")

print("Q-10")
n3 = int(input("Enter a no: "))
if n3%3==0 and n3%7==0:
  print(n3," is a multiple of both 3 and 7")
else:
  print(n3," is not a multiple of both 3 and 7")

print("**Ladder If & Nested If Problems**")

print("Q-1")
no1=int(input("Enter the first no: "))
no2=int(input("Enter the second no: "))
no3=int(input("Enter the third no: "))
if no1>=no2:
  if no1>=no3:
    print(no1," is the greatest")
  else:
    print(no3," is the greatest")
else:
  if no2>=no3:
    print(no2," is the greatest")
  else:
    print(no3," is the greatest")

print("Q-2")
age1=int(input("Enter age: "))
if age1<13:
  print("The person is a Child")
elif age1<=19 and age1>=13:
  print("The person is a Teenager")
elif age1<=59 and age1>=20:
  print("the person is an Adult")
else:
  print("The person is a Senior")

print("Ques-3")
marks=int(input("Enter marks(0-100): "))
if marks>=0 and marks<35:
  print("Fail")
elif marks>=35 and marks<=49:
  print("D")
elif marks>=50 and marks<=74:
  print("C")
elif marks>=75 and marks<=89:
  print("B")
elif marks>=90 and marks<=100:
  print("A")
else:
  print("Enter correct marks")

print("Q-4")
s1=int(input("Enter the first side: "))
s2=int(input("Enter the second side: "))
s3=int(input("Enter the third side: "))
if (s1==s2 and s1!=s3)or(s1==s3 and s1!=s2)or(s2==s3 and s1!=s2):
  print("Its an Isoceles triangle")
elif s1==s2 and s2==s3:
  print("Its an Equilateral traiangle")
else:
  print("Its a Scalene triangle")

print("Q-5")
chars=input("Enter a character: ")
if 'A' <= chars <= 'Z':
  print(chars," is an Uppercase letter")
elif 'a' <= chars <= 'z':
  print(chars," is a Lowercase letter")
elif '0' <= chars <= '9':
  print(chars," is a Digit")
else:
  print(chars," is a Special symbol")

print("Q-6")
unit=int(input("Enter the unit: "))
if unit<=100:
  bill=unit*5
elif unit>100 and unit<=200:
  bill=unit*7
else:
  bill=unit*10
print("Your bill is",bill," for",unit," units")

print("Q-7")
num1=int(input("Enter first no: "))
num2=int(input("Enter second no: "))
num3=int(input("Enter third no: "))
num4=int(input("Enter fourth no: "))
if num1>=num2:
  if num1>=num3:
    if num1>=num4:
      print(num1," is the largest")
    else:
      print(num4," is the largest")
  else:
    if num3>=num4:
      print(num3," is the largest")
    else:
      print(num4," is the largest")
else:
  if num2>=num3:
    if num2>=num4:
      print(num2," is the largest")
    else:
      print(num4," is the largest")
  else:
    if num3>=num4:
      print(num3," is the largest")
    else:
      print(num4," is the largest")

print("Q-8")
years = int(input("Enter the year: "))
if years%400==0:
    print(years, "is a century year and a leap year")
elif years%100==0:
    print(years, "is a century year but not a leap year")
elif years%4==0:
    print(years, "is a leap year")
else:
    print(years, "is not a leap year")

print("Q-9")
bmi=float(input("Enter your bmi: "))
if bmi<18.5:
  print("you are Underweight")
elif bmi>=18.5 and bmi<25:
  print("you are Normal")
elif bmi>=25 and bmi<30:
  print("you are Overweight")
else:
  print("you are Obese")

print("Q-10")
nums1=int(input("Enter first no: "))
nums2=int(input("Enter second no: "))
nums3=int(input("Enter third no: "))
if nums1<=nums2:
  if nums1<=nums3:
    print(nums1,"is the smallest")
  else:
    print(nums3,"is the smallest")
else:
  if nums2<=nums3:
    print(nums2,"is the smallest")
  else:
    print(nums3,"is the smallest")

print("**For-Loop Problems**")

print("Q-1")
for i1 in range(100,1000):
   a=i1%10    #to find ones digit
   a1=i1//10  #to find tens and hundredth digit
   b=a1%10   #to find tens digit
   c=a1//10  #ti find hundreth digit
   sum1=(a**3)+(b**3)+(c**3)
   if sum1==i1:
      print(sum1," ")

print("Q-2")
nu3=int(input("Enter no of prime numbers you want: "))
count=0 
print("First", nu3, "prime numbers are:")
for i in range(2,100000):
    prime=True
    for j in range(2, int(i**0.5) + 1):
        if i % j==0:
            prime=False
            break
    if prime:
        print(i," ")
        count+=1
    if count == nu3:  
        break
    
print("Q-3")
print("Numbers which are divisible by 3 and their digit sum is less than 10 are: ")
for j1 in range(1, 501):
    i=j1
    s=0
    while i>0:
        s+=i%10
        i//=10
    if j1%3==0 and s<=10:
        print(j1," ")

print("Q-4")
rows=int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end=" ")
    for j in range(1,2*i):
        print("*", end="")
    print()

print("Q-5")
st=input("Enter the string: ").lower()
alphabet=set("abcdefghijklmnopqrstuvwxyz")
letters=set(ch for ch in st if ch.isalpha())
if alphabet.issubset(letters):
    print(st,"is a pangram")
else:
    print(st,"is not a pangram")

print("Q-6")
print("Twin primes are: ")
for num in range(2,100):
    pr=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            pr=False
            break
    if pr:
        num2=num+2
        pr2=True
        for i in range(2,int(num2**0.5)+1):
            if num2%i==0:
                pr2=False
                break
        if pr2:
            print(f"({num},{num+2})")

print("Q-7")
num=int(input("Enter a number: "))
sum=0
a=num
while a>0:
    sum+=a%10
    a//=10
if num%sum==0:
    print(num," is a Harshad number")
else:
    print(num," is not a Harshad number")

print("Q-8")
n=int(input("Enter the number of rows: "))
for i in range(n):
    print(" "*(n - i - 1),end="")
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1) 
    print()

print("Q-9")
num=int(input("Enter a number: "))
s=0
for i in range(num+1):
    s+=i**2
print(s," is sum of the series")

print("Q-10")
num=int(input("Enter a number: "))
x=num
sum=0
while x>0:
    d=x%10
    fact = 1
    for i in range(1, d+1):
        fact*=i
    sum+=fact
    x//=10
if sum==num:
    print(num," is a Strong number")
else:
    print(num," is not a Strong number")

print("**While-Loop Problems**")

print("Q-11")
num=int(input("Enter a number: "))
temp=num
rev=0
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp//=10
print("Reversed number is:",rev)
pri=True
if rev<=1:
    pri=False
else:
    i=2
    while i<=rev//2:
        if rev%i==0:
            pri=False
            break
        i+=1
if pri:
    print(rev,"is a prime number")
else:
    print(rev,"is not a prime number")

print("Q-12")
tot=0
while tot<=100:
    num=int(input("Enter a number: "))
    temp=num
    while temp>0:
        dig=temp%10
        tot+=dig
        temp//=10
print("Sum of all digits exceeded 100. Final sum:", tot)

print("Q-13")
num=input("Enter a number: ")
if num[0]=='0':
    print(num,"is not a Duck number")
else:
    i = 0
    found=False
    while i<len(num):
        if num[i]=='0':
            found=True
            break
        i+=1
    if found:
        print(num,"is a Duck number")
    else:
        print(num,"is not a Duck number")

print("Q-14")
num=int(input("Enter a number: "))
seen=[]
x=num
while num!=1 and num not in seen:
    seen.append(num)
    sum=0
    temp=num
    
    while temp>0:
        dig=temp%10
        sum+=dig**2
        temp//=10
    num = sum
if num==1:
    print(x,"is a Happy number")
else:
    print(x,"is not a Happy number")

print("Q-15")
n=int(input("Enter a number: "))
i=2
lp=0
while i<=n:
    if n%i==0:
        prime=True
        j=2
        while j<=i//2:
            if i%j==0:
                prime=False
                break
            j+=1
        if prime:
            lp=i
    i+=1
print("Largest prime factor is:", lp)

print("Q-16")
while True:
    text=input("Enter a string: ")
    if text==text[::-1]:
        print("Palindrome :", text)
        break
    else:
        print("Not a palindrome")

print("Q-17")
num=int(input("Enter a number: "))
while num>=10:
    sum=0
    temp=num
    while temp>0:
        sum+=temp%10
        temp//=10
    num=sum
print("Digital root is:", num)

print("Q-18")
n=int(input("Enter a number for Collatz sequence: "))
while n!=1:
    print(n,end=" → ")
    if n%2==0:
        n=n//2
    else:
        n= (3*n)+1
print(n) 

print("Q-19")
n=int(input("Enter a number: "))
if n==1:
    print(n,"is a Kaprekar number")  
else:
    sq=n*n
    str_sqn=str(sq)
    len_sq= len(str_sqn)
    i=1
    found=False
    while i<len_sq:
        part1_s=str_sqn[:i]
        part2_s=str_sqn[i:]
        if part1_s=="":
            part1=0
        else:
            part1=int(part1_s)

        if part2_s=="":
            part2=0
        else:
            part2=int(part2_s)
        if part1+part2==n and part2!=0:
            found=True
            break
        i+=1
    if found:
        print(n,"is a Kaprekar number")
    else:
        print(n,"is not a Kaprekar number")

print("Q-20")
balance=1000  
while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice=input("Enter your choice (1-4): ")
    if choice=="1":
        print("Current Balance: ₹",balance)
    elif choice=="2":
        amount=int(input("Enter amount to deposit: ₹"))
        if amount>0:
            balance+=amount
            print("₹",amount,"deposited. New balance: ₹",balance)
        else:
            print("Invalid amount")
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: ₹"))
        if amount<=balance:
            balance-=amount
            print("₹",amount,"withdrawn. Remaining balance: ₹",balance)
        else:
            print("Insufficient balance")
    elif choice=="4":
        print("Exiting ATM.\nThank you!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
