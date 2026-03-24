 #1.
 for i in range (1,5):
     if i == 3:
        break #termination
     print(i)

 #2.
 for i in range (1,5):
     if i == 3:
         continue #skips the next statements and goes into next iteration.
     print(i)

 #3.
 #to print
 # 1 5
 # 2 4
 # 4 2
 # 5 1
 for i,j in zip(range(1,6), range(5,0,-1)): #zip is used to iterate two or more iterables together. here it is used to iterate two range functions together.
     if i and j ==3:
         continue
     print(i," ",j)

 #4. 
 #while loop, do while loop is not supported in python.
 i=1
 while i<=5:
     print(i)
     i+=1

 #5. #debug this
 username=""
 password=""

 while username!="Vidhi" and password!="1234":
     print("Invalid username or password. Please try again.")
     break
 username = input("Enter username: ")
 password = input("Enter password: ")
 print("Login successful")

 #6. 
 n=int(input("Enter a number: "))
 sum =0
 i=1
 while i<=n:
     sum+=i
     i+=1
 print("The sum of first",n,"natural numbers is:",sum)

 #7.
 #to remove duplicate characters from a string.
 name = "vidhiharde"
 new_name = ""
 for i in name:
     if i not in new_name:
         new_name+=i
 print(name)
 print(new_name)

 #reverse of a string
 reverse_name = ""
 for i in name:
     reverse_name = i + reverse_name
 print(reverse_name)

 #8.
 mycart =[10,20,200,300,800,60,700]
 for i in mycart:
     if i>400:
         print("This is my cart")
         continue
     print(i)

 #9.
 # #palindrom sequence
 name = "vidhi"
 reverse_name = name[::-1] #slicing method to reverse a string. # what does ::1 mean? it means to take the string in reverse order. the first : means to take the whole string, the second : means to take every character, and the 1 means to take it in reverse order.
 if name == reverse_name:
     print("This is a palindrome sequence.")
 else:
     print("This is not a palindrome sequence.")


 #10.
 #anagram sequence = two words or phrases that are made by rearranging the letters of each other.
 word1 = "listen"
 word2 = "silent"
 if sorted(word1) == sorted(word2): #sorted function is used to sort the characters of the string in alphabetical order. if the sorted characters of both the words are same, then they are anagram sequence.
     print("This is an anagram sequence.")
 else:
     print("This is not an anagram sequence.")

 #11.
 #nested for loops 
 #output :
 #111
 #222
 #333
 for i in range(1,4): #outer loop represents rows
     for j in range(1,4): #inner loop represents columns
         print(i,end=" ") #end="" is used to print the output in the same line. if we don't use end="", then it will print the output in the next line.
     print() #print() is used to move to the next line after each row is printed.

 #12.
 n = int(input("Enter the number of rows: "))
 for i in range(1,n+1):
     for j in range(1,n+1):
         print(chr(64+i),end="")
     print()
