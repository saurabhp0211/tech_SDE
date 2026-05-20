s = "cbaebabacd"
p = "abc"

def allAnagrams(s:str,p:str)->list[int]:
    s1=len(s)
    p1=len(p)
    res=[]
    if s1<p1:
        return []
    

    dict1={}
    for k in range(p1):
        char=p[k]
        dict1[char]=dict1.get(char,0)+1

    dict2={}
    l=0
    for r in range(s1):
        char_r=s[r]
        dict2[char_r]=dict2.get(char_r,0)+1

        while (r-l+1)>p1:
            char_l=s[l]
            dict2[char_l]-=1

            if dict2[char_l]==0:
                del dict2[char_l]
            l+=1
        if dict1==dict2:
            res.append(l)
    return res

print(allAnagrams(s,p))
    
    



    


