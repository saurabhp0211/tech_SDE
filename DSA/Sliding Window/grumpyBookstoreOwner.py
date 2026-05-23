customers=[1,0,1,2,1,1,7,5]
grumpy =  [0,1,0,1,0,1,0,1]
minutes = 3

def grumpy_owner(customers,grumpy, minutes):
    satisfied=0
    max_satisfied=0
    k=len(customers)
    l=0
    for r in range(k):
        if grumpy[r]!=1:
            satisfied+=customers[r]
        elif grumpy[r]!=0:
            satisfied+=customers[r]
        while (r-l+1)>minutes:
            if grumpy[l]==1:
                satisfied-=customers[l]
            l+=1

        max_satisfied=max(satisfied,max_satisfied)

    return max_satisfied

print(grumpy_owner(customers,grumpy,minutes))
        

        

        
    

        
