nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
print(nums)
result=[]

def sum3(nums):
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1
        while l<r:
            sumthree=nums[i]+nums[l]+nums[r]
            if sumthree==0:
                result.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l+1]:
                    l+=1
            
            elif sumthree<0:
                l+=1
            else:
                r-=1
    return result
    
print(sum3(nums))




