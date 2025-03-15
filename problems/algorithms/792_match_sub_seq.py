class Solution(object):
    def numMatchingSubseq(self, s, words):
        def check_subseq(s1,s2):
            i,j = 0,0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i+= 1
                j+=1
            
            return i == len(s1)
        res = 0 
        mem = {}
        for word in words:
            if word in mem:
                res = res + 1 if mem[word] else res
            else:
                bl = check_subseq(word,s)
                res = res + 1 if bl else res
                mem[word] = bl
        return res 

    def numMatchingSubseq0(self, s, words):
        res = 0
        idxs = [0] * len(words)
        for char in s:
            for idx in range(len(words)):

                if idxs[idx] != -1 and idxs[idx] < len(words[idx]) and words[idx][idxs[idx]] == char:
                    idxs[idx] += 1

                if idxs[idx] == len(words[idx]):
                    res += 1
                    idxs[idx] = - 1 

        return res 