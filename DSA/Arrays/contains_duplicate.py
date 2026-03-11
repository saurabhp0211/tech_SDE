nums = [1, 2, 3, 7]
def cont_dupli(nums):
    seen=set()
    
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
        
    
print(cont_dupli(nums))
