class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Complexity: O(1) and O(n)
        """
        for i in range(1, len(sentence) - 1):
            if sentence[i] == " " and (sentence[i-1] != sentence[i+1]):
                return False
        return sentence[0] == sentence[-1]
            