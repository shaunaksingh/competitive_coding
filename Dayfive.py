# #function 
# def msg():
#     print("Hello World")

# def calculate():
#     n1=int(input("Enter the value of n1:"))
#     n2=int(input("Enter the value of n2:"))
#     sum=n1+n2
#     mul=n1*n2
#     sub=n1-n2
#     div=n1/n2
#     return sum, mul, sub, div

# msg()
# sum, mul, sub, div = calculate()
# print("Sum:", sum)
# print("Multiplication:", mul)
# print("Subtraction:", sub)
# print("Division:", div)


# def perosnalInfo(fname,lname):
#     print("First Name:", fname)
#     print("Last Name:", lname)

# perosnalInfo("Kshitij", "Panday")

# def cityName(city):
#     print(city)

# cityName("Delhi")
# cityName("Mumbai")
# cityName("Chennai")


mylist=[5,2,9,7,5,6]
#search the element 7 in the list
def searchElement(element):
    for i in mylist:
        if i==element:
            return True
    return False


print(searchElement(111))
