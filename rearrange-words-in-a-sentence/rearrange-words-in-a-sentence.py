class Solution:
    def arrangeWords(self, text: str) -> str:
        l=text.split(" ")
        l[0] = l[0].lower()
        l.sort(key= len)
        l[0] = l[0][0].upper() + l[0][1:]
            
        return " ".join(l)
