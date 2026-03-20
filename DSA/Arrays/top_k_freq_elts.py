nums = [1,1,1,2,4,4,42,3]
k=2
def top_freq(nums, k):
    seen={}
    for n in nums:
        seen[n]=seen.get(n,0)+1

    buckets=[[] for _ in range(len(nums)+1)]

    for num, count in seen.items():
        buckets[count].append(num)
    
    result=[]
    for i in range(len(buckets)-1,0,-1):
        for num in buckets[i]:
            result.append(num)
            if len(result)==k:
                return result

print(top_freq(nums,k))


