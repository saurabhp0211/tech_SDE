s = "abcabc"

def substrContAll3(s):
    count=0
    l=0
    dict1={'a':0,'b':0,'c':0}
    k=len(s)
    for r in range(k):
        char=s[r]
        dict1[char]=dict1.get(char,0)+1

        while dict1['a']>0 and dict1['b']>0 and dict1['c']>0:
            count+=(k-r)

            char_l=s[l]
            dict1[char_l]-=1
            l+=1

    return count


print(substrContAll3(s))
        



