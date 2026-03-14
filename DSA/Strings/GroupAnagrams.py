strs = ["eat","tea","tan","ate","nat","bat"]

# bruteforce
def isAnagram(s,p):
    if len(s)!=len(p):
        return False
    count={}
    
    for i in range(len(s)):
        count[s[i]]=count.get(s[i],0)+1
        count[p[i]]=count.get(p[i],0)-1

    for val in count.values():
        if val!=0:
            return False
    return True


def anagrams_bf(strs):
    visited=[False]*len(strs)
    result=[]

    for i in range(len(strs)):
        if visited[i]:
            continue
        current_group=[strs[i]]
        visited[i]=True

        for j in range(i+1,len(strs)):

            if isAnagram(strs[i],strs[j]):
                current_group.append(strs[j])
                visited[j]=True
        result.append(current_group)
    return result

print(anagrams_bf(strs))

print("****************")

# O(n)

def grp_anagrams(strs):

    ans={}
    for s in strs:
        key="".join(sorted(s))
    
        if key not in ans:
            ans[key]=[]
        ans[key].append(s)
    print(ans.items())
    return list(ans.values())


print(grp_anagrams(strs))


