s = "AABABBA"
k = 1

def longest_repeating(s:str,k:int)-> int:
    
    longest=0
    l=0
    seen={}
    maxFreq=0
    for r in range(len(s)):
        char=s[r]
        seen[char]=seen.get(char,0)+1
        maxFreq=max(maxFreq, seen[char])

        if (r-l+1)-maxFreq>k:
            seen[s[l]]-=1
            l+=1
        longest=max(longest, r-l+1)
    return longest

print(longest_repeating(s,k))

