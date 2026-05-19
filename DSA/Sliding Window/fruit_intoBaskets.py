fruits = [0,1, 2, 2,3,2]

def fruit_intobaskets(fruits):
    l=0
    baskets={}
    maxl=0
    for r in range(len(fruits)):
        char=fruits[r]
        baskets[char]=baskets.get(char,0)+1
        while len(baskets)>2:
            baskets[fruits[l]]-=1
            if baskets[fruits[l]]==0:
                del baskets[fruits[l]]
            l+=1  
        maxl=max(r-l+1,maxl)

    return maxl

print(fruit_intobaskets(fruits))




        
        


                
        
        
