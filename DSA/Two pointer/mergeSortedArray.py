nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m=3
n=3

def mergeArr(nums1,m,nums2,n):
    i=m-1   #pointer for nums1
    j=n-1   # pointer for nums2
    k=m+n-1   #pointer for nums1 where we will place the element
    while j>=0:
        if i>=0 and nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i-=1
        else:
            nums1[k]=nums2[j]
            j-=1
            k-=1
    
    return nums1

print(mergeArr(nums1,m,nums2,n))            


    
