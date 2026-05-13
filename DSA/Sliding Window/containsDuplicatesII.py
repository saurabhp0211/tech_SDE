nums = [1, 2, 3, 6,1]
k = 3
# brute-force
def contDupli(nums,k):
    for l in range(len(nums)):
        r=l+1
        while (r-l<=k) and r<len(nums):
            if nums[l]==nums[r]:
                return True
            else:
                r+=1
    return False
print(contDupli(nums,k))

# optimised
def containsDupli(nums,k):
    seen={}

    for i, num in enumerate(nums):
        if num in seen:
            if i-seen[num]<=k:
                return True
            
        seen[num]=i
    return False

print(containsDupli(nums,k))

    
