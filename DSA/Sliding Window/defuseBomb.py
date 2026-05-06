code = [5, 7, 1, 4]
k = -2
def decrypt(code,k):
    n=len(code)
    if k==0:
        return [0]*n
    
    extened_code=code+code
    result=[]
    for i in range(n):
        if k>0:
            windowSum=sum(extened_code[i+1:i+1+k])
        else:
            start_index=i+n
            windowSum=sum(extened_code[start_index+k:start_index])
        result.append(windowSum)
    return result

print(decrypt(code,k))