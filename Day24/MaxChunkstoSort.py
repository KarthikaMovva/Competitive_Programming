class Solution(object):
    def maxChunksToSorted(self, arr):
        maxchunks = 0
        chunks = 0

        for i in range(len(arr)):
            maxchunks = max(maxchunks, arr[i])
            if maxchunks == i:
                chunks += 1
    
        return chunks