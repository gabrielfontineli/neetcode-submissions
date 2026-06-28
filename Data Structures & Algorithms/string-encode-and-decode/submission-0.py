class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            size = len(s) 
            result.append(f"{size}#{s}") ## codificando

        return "".join(result)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            size = int(s[i:j]) ## reading size of string from starting point until delimiter index
            result.append(s[j+1:j+1+size]) ## slicing the string, starting from j+1 the very next char from delimiter and stopping at last char of string

            
            i = j + size + 1 ## update index to the next number
        return result

            
            
