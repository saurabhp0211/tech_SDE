customers=[1,0,1,2,1,1,7,5]
grumpy =  [0,1,0,1,0,1,0,1]
minutes = 3


def grummm(customers,grumpy,minutes):
    k=len(customers)
    l=0
    satisfied=0
    bonusPts=0
    max_bp=0
    for r in range(k):
        if grumpy[r]==0:
            satisfied+=customers[r]

        
        if grumpy[r]==1:
            bonusPts+=customers[r]
        
        while (r-l+1)>minutes:
            if grumpy[l]==1:
                bonusPts-=customers[l]
            l+=1
        max_bp=max(bonusPts,max_bp)

    return max_bp+satisfied

print(grummm(customers,grumpy,minutes))
                   