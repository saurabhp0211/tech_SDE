s1,s2 = "ab", "eidbaooao"

def checkInclusion(s1,s2):
    n1=len(s1)
    n2=len(s2)

    need_dict={}
    for char in s1:
        need_dict[char]=need_dict.get(char,0)+1

    for  i in range(n2-n1+1):
        sub=s2[i:i+n1]

        window_dict={}
        for char in sub:
            window_dict[char]=window_dict.get(char,0)+1
        
        if window_dict==need_dict:
            return True
    return False

print(f"Permutation possible: {checkInclusion(s1,s2)} ")


def checkPermutation(s1,s2):
    n1=len(s1)
    n2=len(s2)

    if n1>n2:
        return False
    
    need_dict={}
    for char in s1:
        need_dict[char]=need_dict.get(char,0)+1

    left=0
    window_dict={}
    for right in range(n2):
        char_r=s2[right]
        window_dict[char_r]=window_dict.get(char_r,0)+1

        if (right-left+1)>n1:
            char_l=s2[left]
            window_dict[char_l]-=1

            if window_dict[char_l]==0:
                del window_dict[char_l]
            left+=1
        if window_dict==need_dict:
            return True
    return False

print(f"Permutation possible: {checkPermutation(s1,s2)} ")
    
