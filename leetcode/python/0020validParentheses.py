#"""解决括号匹配的问题 """
class Solution:
    def isValid(self, s):
        """方法主体

        :s: TODO
        :returns: TODO

        """
        stack = []
        map = {
            "{":"}"
            "[":"]"
            "(":")"
                }
        for x in s:
            if x in map:
                stack.append(map[x])
            else:
                if len(stack)!=0:
                    top_element=stack.pop()
                    if x!=top_element:
                        return False
                    else:
                        continue
                    else:
                        return False
        return len(stack) ==0
    
