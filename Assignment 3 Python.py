"""
A. Python IF (Single Condition)

1. Write a Python program to check if a number is positive.

num=int(input("Enter a number:"))
if num>0:
     print("Positive")

     Output =  Enter a number:67
               Positive

     
2. Print "Eligible to vote" if age is 18 or above.

age=int(input("Enter age:"))
if age>18:
    print("Eligible to vote")

    Output = Enter age:45
             Eligible to vote

             
3. Check if a number is divisible by 7.

a= int(input("Enter a number:"))
if a%7==0:
     print(a,"is divisible by 7")

    Output =  Enter a number:56
              56 is divisible by 7
              

4. Print "Pass" if marks are greater than 40.

M=int(input("Enter marks;"))
if M>40:
    print("Pass")

    Output =  Enter marks;56
              Pass
    

5. Check if a number is greater than 100.

num=int(input("Enter a number:"))
if num>100:
    print(num,"is greater than 100")

    Output =  Enter a number:765
              765 is greater than 100


6. Display a message if temperature exceeds 45°C.

T=int(input("Temperature:"))
if T>45:
    print("Temperature exceeds 45°C")

    Output =  Temperature:49
              Temperature exceeds 45°C

   

7. Check if a string length is more than 8 characters.

sl= int(input("Enter string length of a character:"))
if sl>=8:
    print(string length is more than 8 characters)


8. Print "Logged In" if password matches "admin123".

P="admin123"
p=input("Enter a password:")
if p==P:
    print("Logged In")

    Output = Enter a password:admin123
Logged In


    
9. Check if a number is a multiple of 10.

num=int(input("Enter a number:"))
if num%10==0:
    print(num,"is a multiple of 10")

Enter a number:560
560 is a multiple of 10


10. Print a warning if balance is below minimum limit.

balance=float(input("Enter amount:"))
if balance<500:
    print("Low balance")

    Output = Enter amount:456
Low balance
              

B. Python IF–ELSE (Two Conditions)


11. Check whether a number is even or odd.

num=int(input("Enter a number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")

    Output =  Enter a number:456
              Even
              Enter a number:673
              Odd


12. Find the largest of two numbers.
num1=78
num2=87
if num1>2:
    print("Largest number is",num1)
else:
    print("Largest number is",num2)



13. Check whether a person is eligible for driving license.

age=int(input("Enter age:"))
if age>18:
    print("Eligible")
else:
    print("Not Eligible")

    Output = Enter age:23
             Eligible
             Enter age:16
             Not Eligible


14. Print "Pass" or "Fail" based on marks.

marks=int(input("Enter marks:"))
if marks>33:
    print("Pass")
else:
    print("Fail")

    Output =  Enter marks:44
              Pass
              Enter marks:28
              Fail

              
15. Check whether a number is positive or negative.

num=int(input("Enter a number:"))
if num>0:
    print("Positive")
else:
    print("Negative")

    Output =  Enter a number:345
              Positive
              Enter a numbe:-23
              Negative

              
16. Check whether a character is a vowel or consonant.

ch=str(input("Enter a letter:"))
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("Vowel")
else:
    print("Consonant")

    Output = Enter a character:x
             Consonant
             Enter a character:e
             Vowel

                 
17. Check if a year is leap or not.

a = int( input("What's the year:"))

if a%400==0 or a%4==0 and not a%100==0:
    print("Leap year")
    if a%100==0 and not a%400==0:
        print("Not leap year")
else:
    print("Not leap year")

    Output = What's the year:1999
             Not leap year
             What's the year:2032
             Leap year


18. Print "Valid Password" or "Invalid Password".

P =int(input("Enter a Number:"))
if P==123405:
    print("Valid password")
else:
    print("Invalid password")

    Output =  Enter a Number:13245
              Invalid password
              Enter a Number:13245
              Invalid password


19. Determine whether salary is taxable or not.

S =int(input("Enter Salary:"))
if S>500000:
    print("Salary is taxable")
else:
    print("Salary is untaxable")

    Output =  Enter Salary:456635
              Salary is untaxable
              Enter Salary:765433
              Salary is taxable


20. Check whether a number is greater than 50 or not.

num =int(input("Enter a number:"))
if num>50:
    print(num,"is greater than 50")
else:
    print(num,"is not greater than 50")

    Output =  Enter a number:67
              67 is greater than 50
              Enter a number:34
              34 is not greater than 50



C. Python NESTED IF–ELSE

21. Find the largest of three numbers.

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>num2 and num1>num3:
    print(num1,"is greatest")
else:
    if num2>num1 and num2>num3:
        print(num2,"is greatest")
    else:
        print(num3,"is greatest")

    Output =  Enter first number:45
              Enter second number:68
              Enter third number:23
              68 is greatest
              Enter first number:450
              Enter second number:540
              Enter third number:514
              540 is greatest


22. Check whether a number is positive, negative, or zero.

num=int(input("Enter a number:"))
if num==0:
    print("Zero")
else:
    if num>0:
        print("Positive")
    else:
        print("Negative")

    Output =  Enter a number:34
              Positive
              Enter a number:-56
              Negative
              Enter a number:0
              Zero

              

23. Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60

m=int(input("Marks:"))
if m>=90:
    print("Grade:","A")
else:
    if m>=75:
        print("Grade:","B")
    else:
        if m >=60:
            print("Grade","C")
        else:
            print("Fail")

        Output =  Marks:68
                  Grade C
                  
                  Marks:89
                  Grade:B
                  
                  Marks:23
                  Fail
                  
                  Marks:90
                  Grade:A
                  
    

24. Check whether a triangle is equilateral, isosceles, or scalene.

a=float(input("Enter side a:"))
b=float(input("Enter side b:"))
c=float(input("Enter side c:"))
if a + b > c and a + c > b and b + c > a:
       if a==b==c:
           print("equilateral")
       else:
           if a==b or b==c or a==c:
               print("isosceles")
           else:
                print("scalene")
else:
    print("Not a valid triangle")
    Output =   Enter side a:4
               Enter side b:3
               Enter side c:4
               isosceles

               Enter side a:5
               Enter side b:3
               Enter side c:4
               scalene

               Enter side a:7
               Enter side b:2
               Enter side c:5
               Not a valid triangle

               Enter side a:5
               Enter side b:5
               Enter side c:5
               equilateral


    


25. Check whether a character is uppercase, lowercase, digit, or special character.

ch=input("Enter a character:")
if ch .isupper():
    print("Character is uppercase")
else:
    if ch .islower():
        print("Character is lowercase")
    else:
        if ch .isdigit():
            print("Character is digit")
        else:
            print("Character is special character")

        Output =  Enter a character:5
                  Character is digit

                  Enter a character:A
                  Character is uppercase

                  Enter a character:j
                  Character is lowercase

                  Enter a character:%
                  Character is special character
 

26. Calculate electricity bill using slab-wise rates.

a=int(input("What's the usage:"))

if a>=0:
    if a<=100:
       print(a*5)
    else:
        if a>101 and a<=200:
           print((100*5)+(a-100)*10)
        else:
            if a>201 and a<=300:
                print((100*5)+(100*10)+(a-200)*15)
            else:
                print((100*5)+(100*10)+(100*15)+(a-300)*20)

     Output =  What's the usage:654
               10080


27. Validate login using username and password.

un=input("Enter username:")
pw=int(input("Enter password:"))
if un!="Bhoomika Sharma":
    print("Invalid username")
else:
    if pw!=6785:
        print("Invalid password")
    else:
        print("Login successful")
          
    Output =  Enter username:Bhoomika Sharma
              Enter password:3452
              Invalid password

              Enter username:gyjfdgsef
              Enter password:6785
              Invalid username

              Enter username:Bhoomika Sharma
              Enter password:6785
              Login successful
 

28. Check student result using marks of 3 subjects.

n=input("Enter name of student:")
m=int(input("Enter Maths marks:"))
s=int(input("Enter Science Marks:"))
e=int(input("Enter English Marks:"))
tm=m+s+e

if tm>=280:
    print("Grade:","A")
else:
    if tm>=240:
        print("Grade:","B")
    else:
        if tm>=180:
            print("Grade:","C")
        else:
            print("Fail")

    Output =  Enter name of student:Rohan
              Enter Maths marks:78
              Enter Science Marks:65
              Enter English Marks:97
              Grade: B



29. Find the second largest number among three numbers.

n1=int(input("Enter num1:"))
n2=int(input("Enter num2:"))
n3=int(input("Enter num3:"))

if n1>n2 and n1>n3 or n2>n1 and n3>n2 :
    print("Second largest number is",n2)
else:
    if n2>n1 and n2>n3 or n1>n2 and n3>n1:
        print("Second largest number is",n1)
    else:
        print("Second largest number is",n3)
        
    Output =  Enter num1:87
              Enter num2:67
              Enter num3:98
              Second largest number is 87

              Enter num1:466
              Enter num2:3467
              Enter num3:346
              Second largest number is 466



30. Check loan eligibility using age, salary, and credit score.              

a=int(input("Enter age:"))
s=int(input("Enter salary:"))
c=int(input("Enter credit score:"))

if a>=18:
    print("Eligible age")
    if s>=50000:
        print("Eligible salary")
        if c>=500:
            print("Credit score is good")
        else:
            print("Credit score is bad")
    else:
        print("Salary is not enough")
else:
    print("Age should be 17+")
          
    Output =  Enter age:45
              Enter salary:67856
              Enter credit score:300
              Eligible age
              Eligible salary
              Credit score is bad



D. Python ELIF (Multiple Conditions)

31. Print day name using day number (1–7).

a = int(input("Enter position of a day:"))

if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif:
    print("Sunday")
else:
    print("There are only seven days in a week")
    
    Output =  Enter position of a day:5
              Friday

32. Print month name using month number.

a = int(input("Enter position of a month:"))
if a==1:
    print("January")
elif a==2:
    print("February")
elif a==3:
    print("March")
elif a==4:
    print("April")
elif a==5:
    print("May")
elif a==6:
    print("June")
elif a==7:
    print("July")
elif a==8:
    print("August")
elif a==9:
    print("September")
elif a==10:
    print("October")
elif a==11:
    print("November")
elif:
    print("December")
else:
    print("There are only 12 months in a year")
    
    Output =  Enter position of a day:6
              June
              Enter position of a day:12
              December


33. Display grade based on percentage.

a = int(input("Enter percentage:"))
if a==100:
    print("Grade:","A")
elif a>=90:
    print("Grade:","A")
elif a>=75:
    print("Grade:","B")
elif a>=60:
    print("Grade:","C")
elif a>=40:
    print("Grade:","D")
else:
    print("Fail")

    Output = Enter percentage:76
             Grade: B

             Enter percentage:95
             Grade: A

             
34. Display bonus percentage based on experience years.

a = int(input("Experience years:"))
if a>=20:
    print("30%")
elif a>=10:
    print("20%")
elif a>=5:
    print("10%")
else:
    print("5%")

    Output =  Experience years:6
              10%

              Experience years:14
              20%


35. Identify traffic signal meaning.

a = input("Colour of Signal:")
if a=="Green":
    print("GO")
elif a=="Yellow":
    print("Ready")
elif a=="Red":
    print("Stop")
else:
    print(a,"is not a traffic signal")

    Output =  Colour of Signal:Yellow
              Ready

              Colour of Signal:Black
              Black is not a traffic signal


36. Categorize temperature as Cold / Warm / Hot.

a = int(input("Temperature:"))
if a<=20:
    print("Cold")
elif a>=21 and a<=30:
    print("Warm")
elif a>=31 and a<50:
    print("Hot")
else:
    print("Red warning")

    Output =  Temperature:46
              Hot

              Temperature:13
              Cold


37. Categorize employee based on salary range.

a = int(input("Enter Salary:"))
if a>=100000:
    print("Very High Earner")
elif a>=75000 and a<100000:
    print("High Earner")
elif a>=50000 and a<75000:
    print("Very Good Earner")
elif a>=25000 and a<50000:
    print("Good Earner")
elif a>=0 and a<25000:
    print("Entry Level")
else:
    print("Error")

    Output =  Enter Salary:56000
              Very Good Earner


38. Print discount percentage based on purchase amount.

a = int(input("Enter purchase amount:"))
if a>=10000:
    print("25%")
elif a>=7500 and a<10000:
    print("20%")
elif a>=5000 and a<7500:
    print("15%")
elif a>=2500 and a<5000:
    print("10%")
elif a>=0 and a<2500:
    print("5%")
else:
    print("Error")
    Output =  Enter purchase amount:4600
              10%


39. Identify number type: single-digit / double-digit / multi-digit.

a = int(input("Enter purchase amount:"))
if a>=99:
    print(a," is multi-digit number")
elif a>9 and a<99:
    print(a,"is double-digit number")
else:
    print(a,"is single-digit number")
   
    Output =  Enter purchase amount:56
              56 is double-digit number

              Enter purchase amount:4
              4 is single-digit number

              Enter purchase amount:5677
              5677  is multi-digit number


40. Assign performance rating: Poor / Average / Good / Excellent.

a = int(input("Enter performance rating:"))
if a<=100 and a>70:
    print("Excellent")
elif a<70 and a>50:
    print("Good")
elif a<50 and a>30:
    print("Average")
else:
    print("Poor")

    Output = Enter performance rating:67
             Good



E. Python COMPLEX CONDITIONS (AND / OR / NOT)


41. Check whether a number is divisible by 5 and 11.

a=int(input("Enter a number:"))
if a%5==0 and a%11==0:
    print(a,"is divisible by 5 and 11")
else:
    print(a,"is not divisible by 5 and 11")

    Output =  Enter a number:43
              43 is not divisible by 5 and 11

              Enter a number:55
              55 is divisible by 5 and 11


42. Check if a person is eligible for loan: 
● age ≥ 21 
● salary ≥ 25,000 
● credit score ≥ 700

a=int(input("Enter age:"))
s=int(input("Enter salary:"))
c=int(input("Enter credit score:"))
if a>=21 and s>=25000 and c>=700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

    Output =  Enter age:56
              Enter salary:2300
              Enter credit score:600
              Not eligible for loan

              Enter age:36
              Enter salary:44000
              Enter credit score:900
              Eligible for loan


43. Validate login using username AND password.

u=input("Enter username:")
p=int(input("Enter Password:"))

if u=="Bhoomika Sharma" and p==56435 :
    print("Validate")
else:
    print("Invalidate")

    Output =  Enter username:Bhoomika Bhardwaj
              Enter Password:56435
              Invalidate

              Enter username:Bhoomika Sharma
              Enter Password:56435
              Validate


44. Check student pass condition: 
● All subjects ≥ 40 
● Average ≥ 50

e=int(input("Enter English Marks:"))
h=int(input("Enter Hindi Marks:"))
m=int(input("Enter Maths Marks :"))

if e>=40 and h>=40 and m>=40:
    a=(e+h+m)/3
    if a>50:
        print("Pass")
    else:
        print("Fail")

    Output =  Enter English Marks:67
              Enter Hindi Marks:87
              Enter Maths Marks :44
              Pass


45. Check if a number lies between 10 and 100.

n=int(input("Enter number:"))
if n>10 and n<100:
    print(n," is lying between 10 and 100")
else:
    print(n," is not lying between 10 and 100")

    Output =  Enter number:5
              5  is not lying between 10 and 100

              Enter number:56
              56  is lying between 10 and 100


46. Check exam eligibility: 
● attendance ≥ 75% OR 
● medical certificate available

a=int(input("Enter the percentage of attendance:"))
b= input("have any medical certificate available")
if a>=75 and b=="Yes":
    print("Eligible")
else:
    print("Ineligible")
    Output =  Enter the percentage of attendance:87
              have any medical certificate available: Yes
              eligible


47. Validate a date using conditions.


a=int(input("Enter Day:"))
b= int(input("Enter Month:"))
c= int(input("Enter Year:"))
if a<1 or a>31:
    print("Invalid date")
else:
    if b<1 or b>31:
        print("Invalid month")
    else:
        if c<1900 or c>2026:
            print("Invalid Year")
        else:
            print("Date is valid,","Your Date:",a,"/" ,b, "/",c)
    Output = Enter Day:21
             Enter Month:5
             Enter Year:2024
             Date is valid, Your Date: 21 / 5 / 2024

             Enter Day:36
             Enter Month:18
             Enter Year:2004
             Invalid date


48. Check whether an email format is valid.

a=input("Enter Email:")

if ("@")in a and (".") in a:
    print("valid Email")
else:
   print("Invalid Email")

   Output =  Enter Email: sonamsh6754@gmailcom
             valid Email

             Enter Email: sonamsh6754@gmailcom
             Invalid Email

             Enter Email: sonamsh6754gmailcom
             Invalid Email


49. Determine insurance eligibility using age, health status, and income.

a = int( input("Enter age:"))
hs = input("What's the health status(good/avg/bad):")
i = int( input("What's the income:"))

if a>=18 and a<=70 and hs=="good" or hs=="avg" and i>=30000:
    print("Elegiable")
else:
    print("Inelegiable")

    Output =  Enter age:26
              What's the health status(good/avg/bad):good
              What's the income:40000
              Elegiable

              Enter age:87
              What's the health status(good/avg/bad):bad
              What's the income:50000
              Inelegiable
50. Check leap year using complete leap year logic.

a = int( input("Enter year:"))

if a%400==0 or a%4==0 and not a%100==0:
    print("Leap year")
    if a%100==0 and not a%400==0:
        print("Not leap year")
else:
    print("Not leap year")

    Output =  What's the year:2024
              Leap year

              What's the year:1999
              Not leap year



F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS


51. Write a Python program to calculate income tax using slabs.

sal = float(input("Enter Salary:"))
if sal<500000:
    print("No income tax")
else:
    if sal<700000:
        print("Tax:",sal*0.05)
    else:
        if sal<1000000:
            print("Tax:",sal*0.10)
        else:
            print("Tax:",sal*0.15)

    Output =  Enter Salary:600000
              Tax: 30000.0

              Enter Salary:1400000
              Tax: 210000.0


52. Create an ATM withdrawal program with balance checks.

bal=3200
w=float(input("Enter amount withdrwl:"))
if w<=bal:
    print("Collect the money")
    bal=bal-w
    print("Current Balance:",bal)
else:
    print("Insufficient Balance")
    print("Current Balance:",bal)

    Output = Enter amount withdrwl:57000
             Insufficient Balance
             Current Balance: 3200

             Enter amount withdrwl:760
             Collect the money
             Current Balance: 2440.0

53. Check promotion eligibility using experience and performance.

a = float( input("What's the Performance(out of 10):"))
b = float( input("How much Expirence:"))

if a>=7 and b>=10:
    print("Eleigable for promotion")
elif a>3 and b>=5:
    print("fast track to promotion")
else:
    print("Not Elegiable for promotion")

    Output =  What's the Performance(out of 100):98
              How much Expirence:10
              Eleigable for promotion

              What's the Performance(out of 100):87
              How much Expirence:2
              Not Elegiable for promotion


54. Implement a grading system using nested if–else.

a = float( input("What's the marks:"))
if a>=90:
    print("Grade A")
else:
    if a>=70 and a<90:
        print("Grade B")
    else:
        if a>=50 and a<70:
            print("Grade C")
        else:
            if a>=30 and a<50:
                print("Grade D")
            else:
                print("Fail")


    Output = What's the marks:65
             Grade C

55. Validate strong password using multiple conditions.

a = input("Write your password:")
if len(a)<8:
    print("Length of the password is too short")
elif a.lower()==a:
    print("Password doesn't contain an uppercase letter")
elif a.upper()==a:
    print("Password doesn't contain a lowercase letter")
elif not any(char.isdigit() for char in a):
    print("Password should contain a number")
elif not any(char in "~!@$%^&*" for char in a):
    print("Password should contain at least one special character")
else:
    print("Valid password")

    Output =  Write your password:64736$674
              Password doesn't contain an uppercase letter

              Write your password:67465A$64a6
              Valid password


56. Calculate delivery charges based on location and order amount.

a = input("What's the Location(Domestic,International as D and I):")
b = int (input("How much Order Amount:"))

if a=="D" and b<=5000:
    print("Delivery Charges is 3% of amount")
elif a=="I" and b<=10000:
    print("Delivery Charges is 7% of amount")
else:
    print("Free of Charges")

    Output = What's the Location(Domestic,International as D and I):I
             How much Order Amount:6583
             Delivery Charges is 7% of amount


57. Determine online exam qualification.

a = float( input("What's the Attendance:"))
b = float( input("Whats the Internal Marks:"))

if a>=75 and b>=40:
    print("Elegaible for examination")
else:
    print("Inelegaible")

    Output =  What's the Attendance:85
              Whats the Internal Marks:56
              Elegaible for examination


58. Create movie ticket pricing logic based on age & show time.

if a>=18 and b=="D":
    print("Cost the movie ticket is 200")
elif a>=18 and b=="N":
    print("Cost of the movie ticket is 300")
else:
    print("Inelegiable to watch the movie")

    Output =  What's the Age:21
              Whats the time(Day and Night as D and N):D
              Cost the movie ticket is 200


59. Determine bank account type based on balance.

a = float( input("What's the Balance:"))

if a>=10000000:
    print("Premium Account")
elif a>= 1000000 and a<10000000:
    print("Gold Account")
elif a>=100000 and a<1000000:
    print("Silver Account")
else:
    print("Base")

    Output =  What's the Balance:120000000
              Premium Account


60. Create a menu-driven program using if–elif–else.

a = int(input("Whats the number:"))
b = int(input("Whats the number:"))

print(" A.Addition \n B.Subtraction \n C.Multiple \n D.Divison")
c = input("What you wanna do?")
if c == "A":
    print(a+b)
elif c == "B":
    print(a-b)
elif c == "C":
    print(a*b)
elif c == "D":
    print(a/b)
else:
    print("Error")

    Output =  Whats the number:64
              Whats the number:75
               A.Addition
               B.Subtraction
               C.Multiple
               D.Divison
              What you wanna do?A
              139

              Whats the number:48
              Whats the number:6
               A.Addition
               B.Subtraction
               C.Multiple
               D.Divison
              What you wanna do?D
              8.0


              
"""











