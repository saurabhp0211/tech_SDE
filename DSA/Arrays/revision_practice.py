# 3 sum
nums = [-1, 0, 1, 2, -1, -4]

def three_s(nums):
    nums.sort()
    n=len(nums)-1
    result=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=n
        while l<r:
            sum_3=nums[i]+nums[l]+nums[r]
            if sum_3==0:
                result.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
            elif sum_3<0:
                l+=1
            else:
                r-=1
    return result

print(three_s(nums))

            
            



            




    
  

        
    
