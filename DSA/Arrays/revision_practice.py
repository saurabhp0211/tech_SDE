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

            
#longest palindrome substr
s = "forgeeksskeegfor"   
def long_palinstr(s):
    for i in range(len(s)):
        result=""
        l=i
        r=i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>len(result):
                result=s[l:r+1]
            l-=1
            r+=1
        
        l=i
        r=i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>len(result):
                result=s[l:r+1]
            l-=1
            r+=1
    return result
  
# longest concsecutive seq
nums1 = [100, 4, 200, 1, 3, 2]
def longest_seq(nums1):
    longest=0

    num_set=set(nums1)
    for n in num_set:
        if n-1 not in num_set:
            length=1
            while n+length in num_set:
                length+=1
            longest=max(length,longest)
        length=1
    return longest
print(longest_seq(nums1))
    

# top k frequent elements
nums = [1,1,1,2,2,3]
k = 2
def top_kFreq(nums,k):
    seen={}
    for n in nums:
        seen[n]=seen.get(n,0)+1
    buckets=[[] for _ in range(len(nums)+1)]
    result=[]
    for num,count in seen.items():
        buckets[count].append(num)
    for i in range(len(nums)-1,0,-1):
        for num in buckets[i]:
            result.append(num)
            if len(result)==k:
                return result
            
print(top_kFreq(nums,k))


#  subarr sum equals k 
nums = [1, 1, 1]
k = 2
def subarr_sum(nums,k):
    curr_sum=0
    count=0
    seen={0:1}

    for n in nums:
        curr_sum+=n
        diff=curr_sum-k
        if diff in seen:
            count+=seen[diff]
        seen[curr_sum]=seen.get(curr_sum,0)+1
    return count

print(subarr_sum(nums,k))
      

        
          
    


  
        

   
    
