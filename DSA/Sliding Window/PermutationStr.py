s1 = "ab"
s2 = "eidaoobao"

def permutationStr(s1,s2):

    if len(s1)>len(s2):
        return False
    
    target_dict={}
    for i in range(len(s1)):
        char=s1[i]
        target_dict[char]=target_dict.get(char,0)+1

    l=0
    window_dict={}
    for r in range(len(s2)):
        char_r=s2[r]
        window_dict[char_r]=window_dict.get(char_r,0)+1

        while (r-l+1)>len(s1):
            char_l=s2[l]
            window_dict[char_l]-=1

            if window_dict[char_l]==0:
                del window_dict[char_l]
            l+=1
        if window_dict==target_dict:
            return True
    return False

print(permutationStr(s1,s2))
