class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = False
        str1 = "".join(s.split())
        str1 = str1.upper()
        str2 = []
        
        if len(str1) == 0:
            answer = True
        else:
            for i in str1:
                t = ord(i)
                if t > 64 and t < 91:
                    str2.append(i)
                elif t > 47 and t < 58:
                    str2.append(i)
        
        if not answer:
            str1 = "".join(str2)
            str2.reverse()
            str2 = "".join(str2)

            if str1 == str2:
                answer = True
        
        return answer