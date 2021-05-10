class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = defaultdict(int)
        for i in range(len(s) - minSize + 1):
            word = s[i:i + minSize]
            if len(Counter(word)) <= maxLetters:
                cnt[word] += 1
        return max(cnt.values()) if len(cnt) > 0 else 0