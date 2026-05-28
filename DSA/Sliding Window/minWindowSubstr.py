s = "ADOBECOFINJEFIDEBANC"
t = "ABC"

def minWinSubstr(s,t):
    
    minLen=float('inf')
    result=""
    
    target_dict={}
    for i  in range(len(t)):
        char=t[i]
        target_dict[char]=target_dict.get(char,0)+1
    
    for i in range(len(s)):
        needDict={}
        for j in range(i,len(s)):
            char=s[j]
            needDict[char]=needDict.get(char,0)+1

            
            isValid=True
            for t_char in target_dict:
                if needDict.get(t_char,0)<target_dict[t_char]:
                    isValid=False
                    break
            if isValid:
                currLen=j-i+1
                if currLen<minLen:
                    minLen=currLen
                    result=s[i:j+1]
                
    return result

print(minWinSubstr(s,t))

# O(n) soln 

def minWindowSubstr(s,t):
    
    target_Dict={}
    for char in t:
        target_Dict[char]=target_Dict.get(char,0)+1

    have=0
    need=len(target_Dict)
    res=[-1,-1]
    res_len=float('inf')
    l=0
    need_dict={}
    for r in range(len(s)):
        char=s[r]
        need_dict[char]=need_dict.get(char,0)+1

        if char in target_Dict and target_Dict[char]==need_dict[char]:
            have+=1
        
        while have==need:
            if (r-l+1)<res_len:
                res=[l,r]
                res_len=r-l+1
            char_l=s[l]
            need_dict[char_l]-=1

            if char_l in target_Dict and need_dict[char_l]<target_Dict[char_l]:
                have-=1
            l+=1
    l,r=res
    if res_len!=float('inf'):
        return res_len and s[l:r+1]



print(minWindowSubstr(s,t))
    
    
