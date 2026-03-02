s = "ADOBECODEBANC"
t = "ABC"
min_length=float('inf')
result=""

# brute force approach O(n)2

target_count={}
for char in t:
    target_count[char]=target_count.get(char,0)+1


for i in range(len(s)):
    counts={}
    for j in range(i,len(s)):
        char=s[j]
        counts[char]=counts.get(char,0)+1

    is_valid=True
    for t_char in target_count:
        if counts.get(t_char,0)<target_count[t_char]:
            is_valid=False
            break
    if is_valid:
        curr_length=j-i+1
        if curr_length<min_length:
            min_length=curr_length
            result=s[i:j+1]

print(f"The shortest string is {result} and length is {min_length}")

