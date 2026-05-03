nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
def consecutiveOnes(nums,k):
    count=0
    maxl=0
    l=0
    for r in range(len(nums)):
        if nums[r]==0:
            count+=1
        while count>k:
            if nums[l]==0:
                count-=1
            l+=1
        maxl=max(r-l+1,maxl)

    return maxl
    


print(consecutiveOnes(nums,k))