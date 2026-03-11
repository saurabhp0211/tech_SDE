s="anagram"
t="nagar bbam"

def anagrams(s,t):
    if len(s)!=len(t):
        return False
    
    dict1={}
    dict2={}
    for char in s:
        dict1[char]=dict1.get(char,0)+1

    for char in t:
        dict2[char]=dict2.get(char,0)+1

    if dict1==dict2:
        return True
    return False

print(anagrams(s,t))

def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    count={}
    for i in range(len(s)):
        count[s[i]]=count.get(s[i],0)+1
        count[t[i]]=count.get(t[i],0)-1
    for val in count.values:
        if val!=0:
            return False
    return True

print(isAnagram(s,t))




