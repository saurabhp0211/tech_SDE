nums = [1,3,-1,-3,5,3,6,7]
k=3

# brute force
def slidingWin(nums,k):
    l=0
    res=[]
  
    for r in range(l+2,len(nums)):
        maxV=0
        
        maxV=max(nums[l:r+1])
        res.append(maxV)
        while (r-l+1)>k:
            l+=1
        
    return res

print(slidingWin(nums,k))


# O(n)