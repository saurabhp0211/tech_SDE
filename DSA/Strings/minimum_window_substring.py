s = "ADOBECODEBANC"
t = "ABC"
min_length=float('inf')
result=""
max_f=0
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
            curr_l=j-i+1
            if curr_l<min_length:
                min_length=curr_l
                result=s[i:j+1]
            break

print(f"The shortest string is {result} and length is {min_length}")

# O(n)
def min_window(s,t):
    if not t or not s :return ""

    need_dict={}
    for char in t:
        need_dict[char]=need_dict.get(char,0)+1

    
    window_dict={}
    have,need=0,len(need_dict)
    res,res_len=[-1,-1],float("inf")
    l=0

    for r in range(len(s)):
        char=s[r]
        window_dict[char]=window_dict.get(char,0)+1

        if char in need_dict and window_dict[char]==need_dict[char]:
            have+=1

        while have==need:
            if (r-l+1)<res_len:
                res=[l,r]
                res_len=r-l+1

            left_char=s[l]
            window_dict[left_char]-=1

            if left_char in need_dict and window_dict[left_char]<need_dict[left_char]:
                have-=1
            
            l+=1
    l,r=res
    if res_len!=float('inf'):
        return res_len, s[l:r+1]

print(f"O(n) Result: {min_window(s,t)}")



# def min_wind(s,t):
#     if not s or not t: return ""

#     need_dict={}
#     for char in t:
#         need_dict[char]=need_dict.get(char,0)+1

#     need=len(need_dict)
    # have_dict={}
    # have=0
    # res,res_len=[-1,-1],float('inf')
    # l=0

    # for r in range(len(s)):
    #     char=s[r]
    #     have_dict[char]=have_dict.get(char,0)+1

    #     if char in need_dict and have_dict[char]==need_dict[char]:
    #         have+=1
        
    #     while have==need:
    #         if (r-l+1)<res_len:
    #             res=[l,r]
    #             res_len=r-l+1

    #         left_char=s[l]
    #         have_dict[left_char]-=1

#             if left_char in need_dict and have_dict[left_char]<need_dict[left_char]:
#                 have-=1
#             l+=1
#     l,r=res
#     if res_len!=float('inf'):
#         return res_len, s[l:r+1]
#     else:
#         return ""
    

# print(f"O(n) soln {min_wind(s,t)}")


