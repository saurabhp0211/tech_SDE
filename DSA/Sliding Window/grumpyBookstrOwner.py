customers=[1,0,1,2,1,1,7,5]
grumpy =  [0,1,0,1,0,1,0,1]
minutes = 3

def grumpyowner(customers, grumpy, minutes):
    satisfied=0
    maxSatisf=0
    k=len(customers)
    l=0
    for r in range(k):
        if grumpy[r]==0:
            satisfied+=customers[r]
    
    bonus_points=0
    for r in range(k):
        if grumpy[r]==1:
            bonus_points+=customers[r]
        
        while (r-l+1)>minutes:
            if grumpy[l]==1:
                bonus_points-=customers[l]
            l+=1
        
        maxSatisf=max(maxSatisf, bonus_points)
    
    return maxSatisf+satisfied


print(grumpyowner(customers, grumpy,minutes))