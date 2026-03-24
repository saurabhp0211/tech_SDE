nums = [-1, 0, 1, 2, -1, -4]

def three_sum(nums):
    nums.sort()
    result=[]
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1
        while l<r:
            sum_3=nums[l]+nums[r]+nums[i]

            if sum_3==0:
                result.append([nums[i],nums[l],nums[r]])
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
            elif sum_3>0:
                r-=1
            else:
                l+=1
                
    return result

print(three_sum(nums))





