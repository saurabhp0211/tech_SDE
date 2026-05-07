nums = [9, 4, 1, 7,5]
k = 2

def minDiff(nums,k):
    nums.sort()
    res=float('inf')

    for i in range(len(nums)-k+1):
        diff=nums[i+k-1]-nums[i]
        res=min(diff,res)
    return res
    

    
print(minDiff(nums,k))

        


    