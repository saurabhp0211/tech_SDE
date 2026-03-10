s = "cbaebabacd"
p = "abc"

# O(n)
def anagramsFinder(s,p):
    n1=len(p)
    n2=len(s)

    if n1>n2:
        return False

    need_dict={}
    for char in p:
        need_dict[char]=need_dict.get(char,0)+1
    result=[]
    window_dict={}
    l=0
    for r in range(n2):
        char_r=s[r]
        window_dict[char_r]=window_dict.get(char_r,0)+1

        if (r-l+1)>n1:
            char_l=s[l]
            window_dict[char_l]-=1

            if window_dict[char_l]==0:
                del window_dict[char_l]
            l+=1

        if window_dict==need_dict:
            result.append(l)
            
    return result

print(anagramsFinder(s,p))