"""
PART 1 – Basic For Loop Questions 
Q1. Print Numbers 
Use a for loop to print numbers from 1 to 10.

for i in range(1,11):
    print(i)

Output =
1
2
3
4
5
6
7
8
9
10


Q2. Print Even Numbers 
Print all even numbers between 1 and 20.

for i in range(0,21,2):
    if i==0:
        continue
        print(i)
OutPut =
2
4
6
8
10
12
14
16
18
20


Q3. Find Sum 
Print the sum of numbers from 1 to 10 using a for loop.

a=0
for i in range(1,11):
    a=a+i
print(a)
Output =  55


Q4. Multiplication Table 
Take a number from the user and print its multiplication table up to 10.

n=int(input("Enter number:"))
for i in range (1,11):
    print(i*n)

Output =
Enter number:4
4
8
12
16
20
24
28
32
36
40


Q5. Count Characters 
Take a string and count the total number of characters using a for loop.

n="Ramesh"
count=0
for i in n:
    count=count+1
print("Total characters:",count)

Output:-
Total characters: 6



PART 2 – Break Related Questions 
Q6. Stop at 5 
Print numbers from 1 to 10. 
Stop the loop when the number becomes 5.

for i in range(1,10+1):
    if i==5:
        break
    print(i)

Output:-
1
2
3
4


Q7. Search in List 
Search for number 25 in a list. 
If found, print "Found" and stop the loop.

a=[67,356,254,245,52,25,367]
for i in a:
    print(i)
    if i==25:
        print("found:",i)
        break

Output:-
67
356
254
245
52
25
found: 25


Q8. First Negative Number 
Given a list of numbers, print the first negative number and stop the loop.

a=[67,356,-254,245,-52,25,367]
for i in a:
    print(i)
    if i<0:
         print("First negative number is",i)
         break

Output:-
67
356
-254
First negative number is-254


PART 3 – Continue Related Questions 
Q9. Skip 5 
Print numbers from 1 to 10. 
Skip number 5.

for i in range(1,11):
    if i==5:
        continue
    print(i)

Output:-
1
2
3
4
6
7
8
9
10


Q10. Skip Even Numbers 
Print numbers from 1 to 20. 
Skip all even numbers.

for i in range(1,21):
    if i%2==0:
        continue
    print(i)

Output:-
1
3
5
7
9
11
13
15
17
19


Q11. Skip Letter 
Print each character of the string "PYTHON". 
Skip the letter "O". 

a="PYTHOON"
for i in a:
    if i=="O":
        continue
    print(i,end='')

Output:-  PYTHN



PART 4 – Pass Related Questions 
 
Q12. Empty Loop 
Run a loop from 1 to 5 but do nothing inside the loop using pass. 

for i in range(1,6):
    if i==5:
        pass
    print(i)

Output:-
1
2
3
4
5


Q13. Skip Using Pass 
Loop from 1 to 10. 
If number is 6, just use pass. 

for i in range(1,11):
    if i==6:
        pass
    print(i)

Output:-
1
2
3
4
5
6
7
8
9
10



PART 5 – For-Else Questions 
(Remember: else runs only if the loop is not stopped by break.)

Q14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found". 

a=[354,332,243,153,536,478,743]
b=[467,547,34,421,100,141,144]
for i in a:
    if i==100:
        print("Found",i)
    else:
        print("Not found")

Output:-
Not found
Not found
Not found
Not found
Not found
Not found
Not found

a=[354,332,243,153,536,478,743]
b=[467,547,34,421,100,141,144]
for i in b:
    if i==100:
        print("Found",i)
    else:
        print("Not found")

Output:-
Not found
Not found
Not found
Not found
Found 100
Not found
Not found


Q15. Prime Number Check 
Take a number from the user and check whether it is prime using for-else. 
 
count=0 
n=int(input("Enter number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count=count+1
print("Total factors:",count)
if count==2:
    print(n,"is a Prime Number")
else:
    print(n,"is not a Prime Number")

Output:-
Enter number:8
1
2
4
8
Total factors: 4
8 is not a Prime Number

Enter number:7
1
7
Total factors: 2
7 is a Prime Number

 
 
PART 6 – Pattern Questions 
 
Q16. Star Pattern 
Print: 
* 
** 
*** 
**** 
*****

for i in range(1,6):
        print("*"*i)
            
 
Q17. Reverse Star Pattern 
Print: 
***** 
**** 
*** 
** 
* 

for i in range(1,6):
    a=6-i
    print("*"*a)       


Q18. Number Pattern 
Print: 
1 
12 
123 
1234 
12345 
 
a=""
for i in range(1,6):
    a=a+str(i)
    print(a)            


Q19. Same Number Pattern 
Print: 
1 
22 
333 
4444 
55555 

for i in range(1,6):
    print(str(i)*i)       


Q20. Pyramid Pattern 
Print: 
        * 
      *** 
    ***** 
  ******* 
********* 

b=8
a=2
for i in range(1,11,2):
    print(" "*b,"*"*i)
    b=8-a
    a=a+2
    if i==5:
        a=9
   
   
Q21. Inverted Pyramid
Print: 
********* 
  ******* 
    ***** 
      *** 
        *

a=0
b=9
for i in range(1,11,2):
    print(" "*a,"*"*b)
    a=a+2
    b=b-2
   
        
 
Bonus Question 
Q22. Break in Pattern 
Print a star pattern. 
Stop printing when the row number reaches 4.

for i in range(1,6):
        if i==4:
            break
        print("*****")   

Output =
*****
*****
*****


"""















