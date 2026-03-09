str = "ABAABB"
k=1
max_l=0

# brute force O(n)3

for i in range(len(str)):
    for j in range(i,len(str)):
        sub=str[i:j+1]
        counts={}

        for char in sub:
            counts[char]=counts.get(char,0)+1

            curr_len=j-i+1
            max_freq=max(counts.values())

            if curr_len-max_freq<=k:
                if curr_len>max_l:
                    max_l=curr_len

print(max_l)

# brute force O(n)2

for i in range(len(str)):
    counts={}
    for j in range(i,len(str)):
        char=str[j]
        counts[char]=counts.get(char,0)+1

        max_fr=max(counts.values())
        currn_l=j-i+1

        if currn_l-max_fr<=k:
            max_l=max(max_l,currn_l)
        else:
            break


print(max_l)

# optimised O(n)
counts={}
left=0
for right in range(left,len(str)):
        char_r=str[right]
        counts[char_r]=counts.get(char_r,0)+1

        while (right-left+1)-max(counts.values())>k:
            char_l=str[left]
            counts[char_l]-=1

            left+=1

        max_l=max(max_l,right-left+1)

print(f"the longest repeating char length is {max_l}")

        
        



