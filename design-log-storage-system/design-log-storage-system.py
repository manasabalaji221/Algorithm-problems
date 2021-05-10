class LogSystem:

    def __init__(self):
        arr = ["Year", "Month", "Day", "Hour", "Minute", "Second"]
        self.mapping = {j:i for i,j in enumerate(arr)}
        self.array = []
        self.id = {}

    def put(self, id: int, timestamp: str) -> None:
        t = tuple(timestamp.split(':'))
        self.id[t] = id
        bisect.insort(self.array, t)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        i = self.mapping[granularity]
        sl = start.split(':')
        el = end.split(':')
        for j in range(i+1,6):
            sl[j] = '00'
            el[j] = '59'
        st, et = tuple(sl), tuple(el)
        left = bisect.bisect_left(self.array, st)
        right = bisect.bisect_right(self.array, et)
        ans = []
        for i in range(left,right):
            ans += self.id[self.array[i]],
        return ans


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)