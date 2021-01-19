class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sen=sentence.split(" ")
        # print(sen)
        l=len(searchWord)
        print(l)
        for i in sen:
            # print(i)
            if(len(i)>=l):
                s=i[:l]
                # print(s)
                if(i[:l]==searchWord):
                    return sen.index(i)+1
            
        return -1
                    
                
