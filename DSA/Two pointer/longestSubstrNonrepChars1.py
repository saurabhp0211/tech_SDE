s=s = "abcabcbb"
def longestSubstr(s):
    set1=set()
    l=0
    maxL=0
    for r in range(len(s)):
        while s[r] in set1:
            set1.remove(s[l])
            l+=1
        set1.add(s[r])
        maxL=max(r-l+1,maxL)
    
    return maxL

print(longestSubstr(s))
                 