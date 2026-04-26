height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
def trappedRain(height):

    l=0
    r=len(height)-1
    lmax=height[l]
    rmax=height[r]
    trappedWater=0
    while l<r:
            
        if lmax<rmax:
            l+=1
            if height[l]>lmax:
                lmax=height[l]
            else:
                trappedWater+=lmax-height[l]
        else:
            r-=1
            if height[r]>rmax:
                rmax=height[r]
            else:
                trappedWater+=rmax-height[r]
    return trappedWater


print(trappedRain(height))
