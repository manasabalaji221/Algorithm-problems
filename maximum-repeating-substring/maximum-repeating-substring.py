class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        c = 0
        
        for k in range(1, (len(sequence) // len(word)) + 1):
            word_k = k*word
            
            try:
                word_k_index = sequence.index(word_k)
                if k > c:
                    c = k
                
            except:
                break                
        return(c)