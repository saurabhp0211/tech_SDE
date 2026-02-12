# reverse a string **************
# str="forge"
# result=" "
# for ch in str:
#     result=ch+result

# print(result)

# print("got the string reversed")
# print("Dfdf")

# reverse a number  ******************

# num1=3456343
# temp=0
# while num1>0:
#     temp=temp*10
#     temp=temp+num1%10
#     num1=num1//10
# else:
#     print(temp)

# count digits in a number  **************

# count=0
# if num1==0:
#     count=1
# while num1>0:
#     num1=num1//10
#     count=count+1

# print(count)

# palindrome string   **********  two pointer method

# strr="racecar"
# i=0
# j=len(strr)-1
# isPalindrome=True
# while i<j:
#     if(strr[i]==strr[j]):
#         i=i+1
#         j=j-1
#     else:
#         isPalindrome=False
#         break

# if isPalindrome:
#     print("The string is a palindrome")
# else:
#     print("its not a palindrome")

# manual method   **********
# str="racecar"
# revstr=""
# for i in range(len(str)-1,-1,-1):
#     revstr=revstr+str[i]

# if(revstr==str):
#     print("palin")
# else:
#     print("not a palin")


# manual method2   ****************
# for ch in str:
#     revstr=ch+revstr

# if revstr==str:
#     print("its a palin")
# else:
#     print("not a palin")

# palindrome string with empty spaces and upper/lowercase  *******************

# srr="A m  an a plan a canal Panama"
# cleanstr=""
# i=0
# for x in srr:
#     if(x!=" "):
#         cleanstr=cleanstr+x.lower()

# revss=""
# for i in range(len(cleanstr)-1,-1,-1):
#     revss=revss+cleanstr[i]

# if(revss==cleanstr):
#     print("its a palin")
# else:
#     print("its not a palin")

# count vowels and consonants  ************
# str="HIsaurabh where are you going"
# str=str.lower()
# print(str)

# c_count=0
# v_count=0
# vowels="aeiou"

# for ch in str:
#     if 'a'<= ch <='z':
#         is_vowel=False
#         for v in vowels:
#             if ch==v:
#                 is_vowel=True
#                 break
#         if is_vowel:
#             v_count=v_count+1
#         else:
#             c_count=c_count+1

# print(f"Vowel count is {v_count}")
# print(f"Consonants count is {c_count}")


# practicing vow and cons again ******
# stt="hi im saurabh im preparing for sde roles"
# stt=stt.lower()
# v_Count=0
# c_Count=0
# vowels="aeiou"
# for ch in stt:
#     if 'a'<=ch<='z':
#         is_vowel=False
#     for v in vowels:
#         if ch==v:
#             is_vowel=True
#             break
            
#     if is_vowel:
#         v_Count=v_Count+1
#     else:
#         c_Count=c_Count+1
            

# print(f"Vowels count is {v_Count}")
# print(f"Consonants count is {c_Count}")

# find max and second max *****************************
# max
# l1=[34,5,33,23,56,96,18]
# max=0
# for i in range(len(l1)-1,-1,-1):
#     if l1[i]>max:
#         max=l1[i]
    
# print(max)

# find 2nd max 
# max1=float('-inf')
# max2=float('inf')

# nums=[45,66,789,12,34]

# for n in nums:
#     if n>max1:
#         max2=max1
#         max1=n
#     elif n>max2 and n!=max1:
#         max2=n
# if max2==float('-inf'):
#     print("There is no second largest number")
# else:
#     print(f"The second largest number is {max2}")
        
