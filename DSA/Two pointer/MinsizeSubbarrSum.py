nums = [2, 3, 1, 2, 4, 3]
target=7

def minSubarr(nums,target):
    minLen=float('inf')
    curSum=0
    l=0
    
    for r, n in enumerate(nums):
        curSum+=n
        while curSum>=target:
            minLen=min(minLen,r-l+1)

            curSum-=nums[l]
            l+=1
        
        
    return minLen if minLen!=float('inf') else 0

print(minSubarr(nums,target))
