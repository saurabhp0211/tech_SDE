nums = [1, 2, 3, 4]

# def product_except_self(nums):
#     n=len(nums)
#     answer=[1]*n

#     for i in range(n):
#         curr_product=1
#         for j in range(n):
#             if j!=i:
#                 curr_product*=nums[j]
#         answer[i]=curr_product    
#     return answer

# print(product_except_self(nums))

# O(n)
def prod_except_self(nums):
    n=len(nums)
    result=[1]*n

    prefix=1
    for i in range(n):
        result[i]=prefix
        prefix*=nums[i]

    suffix=1
    for i in range(n-1,-1,-1):
        result[i]*=suffix
        suffix*=nums[i]
    return result

print(prod_except_self(nums))
