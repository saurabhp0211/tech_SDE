nums = [1,2,1,2,3]
k = 2

def atmostK(nums,k):
    l=0
    container={}

    total_subarr=0
    for r in range(len(nums)):
        char=nums[r]
        container[char]=container.get(char,0)+1

        while len(container)>k:
            char_l=nums[l]
            container[char_l]-=1

            if container[char_l]==0:
                del container[char_l]
            l+=1
        total_subarr+=r-l+1
    return total_subarr

print(atmostK(nums,k))


        
    
    
    