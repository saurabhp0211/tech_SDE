code=[5,7,1,4]
k=3
def decrypt(code,k):
    n=len(code)
    res=[0]*n
    currSum=0
    if k==0:
        return res
    
    l,r=(1,k) if k>0 else(n+k ,n-1)

    for i in range(l,r+1):
        currSum+=code[i%n]
    
    for i in range(n):
        res[i]=currSum

        currSum-=code[l%n]
        l+=1
        r+=1
        currSum+=code[r%n]
    return res

print(decrypt(code,k))
                   
