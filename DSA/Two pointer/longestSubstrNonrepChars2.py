s=s = "abcabcbb"
def longestSubstr(s):
    l=0
    maxl=0
    seen={}
    for r in range(len(s)):
        char=s[r]
        if char in seen and seen[char]>=l:
            l=seen[char]+1
        
        seen[char]=r
        maxl=max(r-l+1,maxl)
    return maxl

print(longestSubstr(s))
