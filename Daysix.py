# fruit_list1 = ['Apple','Banana','Cherry','Papaya','Mango']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]

# # Modify only first element
# fruit_list1[0] = 'Grapes'

# # Modify second element ONLY in fruit_list1 using copy trick
# fruit_list1 = fruit_list1[:]   # break reference with fruit_list2
# fruit_list1[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Grapes':
#         sum += 1
#         if ls[1] == 'Kiwi':
#             sum += 20

# print(sum)


# def f(i, values = []):
#     values.append(i)
#     print(values)

# f(1)
# f(2)
# f(3)


# def func(value, values):
#     var = 1
#     values[0] = 44
#     t = 3
#     v = [1, 2, 3]
#     print(t, v[0])

# # calling the function
# value = 5
# values = [10, 20, 30]

# func(value, values)

# # to see the change in list
# print(values)

# dict={'c':97, 'a':96, 'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# fruit ={}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))


#q10 product of array except self:
   

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # Left pass
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Right pass
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
