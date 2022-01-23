class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        
        for str in strs[1:]:
            buff = ""
            if not output:
                break
            
            if len(output) <= len(str):
                for i in range(0, len(output)):
                    if output[i] == str[i]:
                        buff += str[i]
                    else:
                        break
            else:
                for i in range(0, len(str)):
                    if output[i] == str[i]:
                        buff += str[i]
                    else:
                        break
            
            output = buff
        
        return output