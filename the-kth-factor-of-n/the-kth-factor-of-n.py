class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i, big = 1, []
        while k > 0 and i*i <= n:
            if n % i == 0:
                k -= 1
                if n // i != i: big.append(n // i)
            i += 1
        if k == 0: return i-1          
        if len(big) >= k : return big[-k]
        return -1 