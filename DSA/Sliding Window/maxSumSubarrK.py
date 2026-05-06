nums = [2, 1, 5, 1, 3, 2]
k = 3
def maxSubarrsum(nums,k):
    currSum=sum(nums[:k])
    maxSum=currSum

    for i in range(k,len(nums)):
        currSum+=nums[i]-nums[i-k]

        maxSum=max(currSum,maxSum)

    return maxSum


print(maxSubarrsum(nums,k))
        



    
