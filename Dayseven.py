import re
var = 'shaunak@1943548!vnr*'
count = 0
for i in var:
    z = ord(i)
    if z>=97 and z<=122:
        continue
    elif z>=48 and z<=57:
        continue
    else:
        count+=1
print(count)

#q-15
# Find intersection of three arrays
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
arr3 = [3, 4, 5]

for i in arr1:
    if i in arr2 and i in arr3:
        print(i)

# q-11: Move zeros to the end
arr = [0, 1, 0, 3, 12]
non_zero_index = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[non_zero_index] = arr[i]
        non_zero_index += 1

for i in range(non_zero_index, len(arr)):
    arr[i] = 0

print(arr)


# #q-2 find the Second largest element:
# arr = [10, 5, 20, 8, 15]
# largest = float('-inf')
# second_largest = float('-inf')

# for num in arr:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num

# print(second_largest)

#question : write a program to calculate the sum of disctances between the adjacent numbers in an array of positive integers:
# def total_distance(n, arr):
#     total = 0
#     for i in range(n - 1):
#         total += abs(arr[i] - arr[i + 1])
#     return total

# arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
# print(total_distance(len(arr), arr))

# N = int(input())
# sum=0
# mylist=[]
# for i in range(N):
#     a = int(input('Enter element value:'))
#     mylist.append(a)
# for j in range(len(mylist)):
#     if j+1 in range(len(mylist)):
#         sum+= abs(mylist[j]-mylist[j+1])
# print(sum)
