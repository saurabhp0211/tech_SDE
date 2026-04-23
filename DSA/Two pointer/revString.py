strr="eventful"
l1=list(strr)
print(l1)

def revstr(l1):
    l=0
    r=len(l1)-1
    while l<r:
        l1[l],l1[r]=l1[r],l1[l]
        l+=1
        r-=1
    
    return "".join(l1)

print(revstr(l1))