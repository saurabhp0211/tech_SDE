code = [5, 7, 1, 4]
k = -2
def decrypt(code,k):
    n=len(code)
    if k==0:
        return [0]*len(code)
    
    extended_code=code+code
    result=[]
    for i in range(len(code)):
        if k>0:
            windowSum=sum(extended_code[:k+i+1])
        else:
            start_index=i+n
            windowSum=sum(extended_code[start_index+k:start_index])
        result.append(windowSum)
    
    return result

print(decrypt(code,k))