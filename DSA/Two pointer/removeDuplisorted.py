nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
def removeDuplicatesSortedArr(nums):
    if not nums:
        return 0
    
    i=0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return i+1

k=removeDuplicatesSortedArr(nums)
print(f"the count of unique elts{k}")
print(f"The updated array {nums[:k]}")




    
    


    
            