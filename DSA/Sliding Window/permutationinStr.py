s1 = "ab"
s2="eidobaoao"

def permutationStr(s1,s2):
    n1=len(s1)
    n2=len(s2)
    if n2<n1:
        return False
    
    dict_req={}
    for k in range(n1):
        char=s1[k]
        dict_req[char]=dict_req.get(char,0)+1
    
    left=0
    window_dict={}
    for right in range(n2):
        char_r=s2[right]
        window_dict[char_r]=window_dict.get(char_r,0)+1

        while ((right-left+1)>n1):
            char_l=s2[left]
            window_dict[char_l]-=1

            if window_dict[char_l]==0:
                del window_dict[char_l]
            left+=1
        
        if window_dict==dict_req:
            return True
        
    return False

print(permutationStr(s1,s2))