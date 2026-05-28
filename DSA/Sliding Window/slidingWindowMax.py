import collections

nums = [1,3,-1,-3,5,3,6,7]
k=3

# brute force
def slidingWin(nums,k):
    l=0
    res=[]
  
    for r in range(l+2,len(nums)):
        maxV=0
        
        maxV=max(nums[l:r+1])
        res.append(maxV)
        while (r-l+1)>k:
            l+=1
        
    return res

print(slidingWin(nums,k))


# O(n)

def sliding_win_Max(nums,k):
    res=[]
    q=collections.deque()

    for r in range(len(nums)):
        while q and nums[q[-1]]<nums[r]:
            q.pop()
        q.append(r)

        if q[0]<(r-k+1):
            q.popleft()
        if r>=k-1:
            res.append(nums[q[0]])
    return res

print(sliding_win_Max(nums,k))