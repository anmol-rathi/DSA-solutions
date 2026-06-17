class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={ "]":"[", "}":"{", ")":"("}
        for i in s:
            if stack and (i in hashmap and hashmap[i]==stack[-1]):
                stack.pop()
            else:
                stack.append(i)
        return not stack
