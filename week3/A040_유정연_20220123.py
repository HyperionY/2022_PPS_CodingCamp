class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        answer = False
        vowel_list = "aeiouAEIOU"
        half = int(len(s)/2)
        s1 = s[:half]
        s2 = s[half:]
        s1_numVowel = 0
        s2_numVowel = 0
        
        for i in s1:
            if i in vowel_list:
                s1_numVowel += 1
        for j in s2:
            if j in vowel_list:
                s2_numVowel += 1
        
        if s1_numVowel == s2_numVowel:
            answer = True
        
        return answer