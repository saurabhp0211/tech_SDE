s="A man, a plan, a canal: Panama"
def remove_literals(s):
    s1=""
    for char in s:
        if char.isalnum():
            s1+=char.lower()
    return s1
cleaned_str=remove_literals(s)
def valid_palindrome(cleaned_str):
    l=0
    r=len(cleaned_str)-1
    is_palindrome=True

    while l<r:
        if cleaned_str[l]!=cleaned_str[r]:
            is_palindrome=False
            break
        l+=1
        r-=1
    return is_palindrome

print(valid_palindrome(cleaned_str))



