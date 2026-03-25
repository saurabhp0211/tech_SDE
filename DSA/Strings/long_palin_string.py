s = "babad"
def longest_palindromic_substr(s):
    res=""
    for i in range(len(s)):
        l=i
        r=i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>len(res):
                res=s[l:r+1]
            l-=1
            r+=1
        
        l=i
        r=i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>len(res):
                res=s[l:r+1]
            l-=1
            r+=1
    return res
    
print(longest_palindromic_substr(s))




