height = [3,0,2]
lmax=height[0]
rmax=height[-1]
Wmax=0
def trappedWater(height):
    for i in range(len(height)-1):
        Wcurr=min(lmax,rmax)-height[i]
        Wmax=max(Wcurr,Wmax)

        if height[i]>lmax:
            
