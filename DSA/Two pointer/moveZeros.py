nums = [2,0, 1, 0, 3, 0,55,12]
def zerosToend(nums):
    i=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            
    return nums

print(zerosToend(nums))