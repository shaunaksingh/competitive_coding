#1
for i in range (1,5):
    if i == 3:
        break
    print(i)

#2
for i in range (1,5):
    if i == 3:
        continue
    print(i)

#3
for i,j in zip(range(1,6), range(5,0,-1)):
    if i and j ==3:
        continue
    print(i," ",j)

#4
i=1
while i<=5:
    print(i)
    i+=1

#5 (fixed login program)
username=""
password=""

while username!="Shaunak" or password!="1234":
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username!="Shaunak" or password!="1234":
        print("Invalid username or password. Please try again.")

print("Login successful")

#6
n=int(input("Enter a number: "))
sum =0
i=1
while i<=n:
    sum+=i
    i+=1
print("The sum of first",n,"natural numbers is:",sum)

#7 remove duplicate characters
name = "Shaunaksingh"
new_name = ""
for i in name:
    if i not in new_name:
        new_name+=i
print(name)
print(new_name)

#reverse string
reverse_name = ""
for i in name:
    reverse_name = i + reverse_name
print(reverse_name)

#8
mycart =[10,20,200,300,800,60,700]
for i in mycart:
    if i>400:
        print("This is my cart")
        continue
    print(i)

#9 palindrome
name = "Shaunak"
reverse_name = name[::-1]
if name == reverse_name:
    print("This is a palindrome sequence.")
else:
    print("This is not a palindrome sequence.")

#10 anagram
word1 = "listen"
word2 = "silent"
if sorted(word1) == sorted(word2):
    print("This is an anagram sequence.")
else:
    print("This is not an anagram sequence.")

#11 nested loop
for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()

#12
n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end="")
    print()
