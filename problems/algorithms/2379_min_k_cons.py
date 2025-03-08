class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_k = float("inf")
        for i in range(0, len(blocks) - k + 1):
            curr_k = 0

            for j in range(i, i + k ):
                if blocks[j] == "W":
                    curr_k += 1

            if curr_k < min_k:
                min_k = curr_k

        return min_k