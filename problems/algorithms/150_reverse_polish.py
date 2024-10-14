from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Complexity: O(n)
        """
        operands = {"+": lambda x,y : x+y,
                    "-": lambda x,y : x-y,
                    "*": lambda x,y : x*y,
                    "/": lambda x,y : int(x/y)
                    }
        elements = []
        for element in tokens:
            if element in operands:
                a, b = elements.pop(), elements.pop()
                elements.append( operands[element](b, a) )
            else:
                elements.append( int(element) )

        return elements[0]
        
