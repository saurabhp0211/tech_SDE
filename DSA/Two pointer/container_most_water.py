height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
def most_containers(height):
    l=0
    r=len(height)-1
    maxArea=0
    for i in range(len(height)-1):
        w=r-l
        currArea=w*(min(height[l],height[r]))
        maxArea=max(maxArea,currArea)
        if height[l]>height[r]:
            r-=1
        else:
            l+=1
    return maxArea

print(most_containers(height))





    
