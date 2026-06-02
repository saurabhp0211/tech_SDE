nums = [1,2,1,2,3]
k = 2

def subarrKdiffInts(nums,k):
    return atmost(nums,k)-atmost(nums,k-1)


def atmost(nums,k):
    dict1={}
    l=0
    subarrays=0
    for r in range(len(nums)):
        char=nums[r]
        dict1[char]=dict1.get(char,0)+1

        while len(dict1)>k:
            char_l=nums[l]
            dict1[char_l]-=1

            if dict1[char_l]==0:
                del dict1[char_l]
            l+=1
        subarrays+=(r-l+1)
        
    return subarrays

print(subarrKdiffInts(nums,k))
        
    
    
    