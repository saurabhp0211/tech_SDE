nums = [-4, -1, 0, 3, 10]

def sorted_squares(nums):
    n=len(nums)
    res=[0]*n
    l=0
    r=n-1
    for i in range(n-1,-1,-1):
        if abs(nums[l])<abs(nums[r]):
            res[i]=nums[r]**2
            r-=1
        else:
            res[i]=nums[l]**2
            l+=1
    return res

print(sorted_squares(nums))