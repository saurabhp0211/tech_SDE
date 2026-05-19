nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k=2

def maxConsecOnesIII(nums,k):
    l=0
    count=0
    maxCLen=0
    for r in range(len(nums)):
        if nums[r]==0:
            count+=1
        while count>k:
            if nums[l]==0:
                count-=1
            l+=1
        maxCLen=max(r-l+1,maxCLen)
    
    return maxCLen


        
    

print(maxConsecOnesIII(nums,k))
