nums = [2, 7, 11, 15]
target = 9

def twosumII(nums,target):
    l=0
    r=len(nums)-1
    currSum=0
    while l<r:
        currSum=nums[l]+nums[r]

        if currSum==target:
            return [l+1,r+1]
        elif currSum<target:
            l+=1
        else:
            r-=1
    return []
    
print(twosumII(nums,target))

        
