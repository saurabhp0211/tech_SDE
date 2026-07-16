strs=["neet", "code", "love", "you"]

class Solution:
    def encode(self, strs:list[str])->str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        
        return res
    

    def decode(self, encoded_str:str)->list[str]:
        i=0
        res=[]
        # first thing we will do is find #

        while i<len(encoded_str):
            j=i
            while encoded_str[j]!='#':
                j+=1

            length=int(encoded_str[i:j])

            word=encoded_str[j+1:j+1+length]
            res.append(word)

            i=j+1+length
        return res
    


sol=Solution()

encoded_str=sol.encode(strs)
decoded_str=sol.decode(encoded_str)
print(encoded_str)
print("")
print(decoded_str)

