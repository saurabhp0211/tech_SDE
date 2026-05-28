s="A man, a plan, a canal: Panama"
def clean_literals(s):
    s1=""
    for char in s:
        if char.isalnum():
            s1+=char.lower()
    return s1
cleaned_str=clean_literals(s)

def valid_palin(cleaned_str):
    l=0
    is_palin=True
    r=len(cleaned_str)-1
    
    while l<r:
        if cleaned_str[l]!=cleaned_str[r]:
            is_palin=False
            break
        l+=1
        r-=1
    return is_palin

print(valid_palin(cleaned_str))


# product array except self 

nums=[1,2,3,4]
n=len(nums)
result=[1]*n
prefix=1
for i in range(n):
    result[i]=prefix
    prefix*=nums[i]

suffix=1
for i in range(n-1,-1,-1):
    result[i]*=suffix
    suffix*=nums[i]

print(result)
