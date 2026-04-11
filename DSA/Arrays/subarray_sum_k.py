nums = [1, 2, 3]
k = 3

def subarr_sum(nums,k):
    count=0
    current_sum=0
    seen={0:1}


    for n in nums:
        current_sum+=n

        diff=current_sum-k

        if diff in seen:
            count+=seen[diff]
        seen[current_sum]=seen.get(current_sum,0)+1
    return count


print(subarr_sum(nums,k))


def subarr_s(nums,k):
    curr_s=0
    seen={0:[-1]}
    result=[]

    for i,n in enumerate(nums):
        curr_s+=n
        diff=curr_s-k

        if diff in seen:
            for old_idx in seen[diff]:
                subarray=nums[old_idx+1:i+1]
                result.append(subarray)
        if curr_s not in seen:
            seen[curr_s]=[]
        seen[curr_s].append(i)
    return result

print(subarr_s(nums,k))