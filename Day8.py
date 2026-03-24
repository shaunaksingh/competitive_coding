# def addition(a, b):
#     print(f"Result: {a + b}")

# def subtraction(a, b):
#     print(f"Result: {a - b}")

# def multiplication(a, b):
#     print(f"Result: {a * b}")

# def division(a, b):
#     if b == 0:
#         print("Error: Cannot divide by zero!")
#     else:
#         print(f"Result: {a / b}")

# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     val1 = float(input("Enter the first number: "))
#     val2 = float(input("Enter the second number: "))
#     choice = input("Enter your choice: ")
#     if choice == '1':
#         addition(val1, val2)
#     elif choice == '2':
#         subtraction(val1, val2)
#     elif choice == '3':
#         multiplication(val1, val2)
#     elif choice == '4':
#         division(val1, val2)
#     elif choice == '5':
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice. Please try again.")
        
# def outerfunction():
#     print("This is the outer function.")
    
#     def innerfunction():
#         print("This is the inner function.")
    
#     innerfunction()
# outerfunction()

# name = "Alice is the best programmer in the world"
# count = 1
# for i in name:
#     if i == 'a' or i == 'A':
#         count += 1
#     else:
#         continue
# print(f"The number of 'a' or 'A' in the string is: {count - 1}")

# init_tuple_a = '1','2'
# init_tuple_b    = ('3','4')
# print(init_tuple_a)
# print(init_tuple_b)

# s=""
# s1=s.replace("difficult ","easy")
# print(s1)
# s="ababababababbaba"
# s1=s.replace("ab","cd")
# print(s1)   

city=input("Enter the name of city: ")
scity=city.strip()
if scity == "hyderabad":
    print("The city is Hyderabad")
elif scity == "delhi":
    print("The city is Delhi")
elif scity == "mumbai":
    print("The city is Mumbai")
elif scity == "chennai":
    print("The city is Chennai")
