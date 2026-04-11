nums = [2, 7, 11, 15]
target = 9
def two_s(nums,target):
    seen={}
    for i in range(len(nums)):
        rem=target-nums[i]
        if rem in seen:
            return [seen[rem],i]
        seen[nums[i]]=i
    return False

print(two_s(nums,target))

def two_ss(nums,target):
    seen={}
    for i,num in enumerate(nums):
        rem=target-num
        if rem in seen:
            return [seen[rem],i]
        seen[num]=i
    return False

print(two_ss(nums,target))
