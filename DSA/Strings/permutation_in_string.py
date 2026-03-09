s1,s2 = "ab", "eidbooao"

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



