str="saurabh"
def revstr(str):
    chars=list(str)
    i=0
    j=len(str)-1
    while i<j:
        chars[i],chars[j]=chars[j],chars[i]
        i+=1
        j-=1
    return "".join(chars)
    

print(revstr(str))

