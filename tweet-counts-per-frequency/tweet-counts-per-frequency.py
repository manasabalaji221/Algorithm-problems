class TweetCounts:

    def __init__(self):
        self.tweets={}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if(tweetName not in self.tweets):
            self.tweets[tweetName]=[time]
        else:
            self.tweets[tweetName].append(time)
        # print(self.tweets)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        # print("get")
        if(freq=="minute"):
            c=0
            x=60
            # print(self.tweets[tweetName])
            m = ((endTime-startTime)//60 )+1
            freq=[0]*m
            for i in sorted(self.tweets[tweetName]):
                if(i>=startTime and i<=endTime):
                    freq[(i-startTime)//60]+=1
            return freq
        
        elif(freq=="hour"):
            c=0
            x=60
            # print(self.tweets[tweetName])
            m = ((endTime-startTime)//3600 )+1
            freq=[0]*m
            for i in sorted(self.tweets[tweetName]):
                if(i>=startTime and i<=endTime):
                    freq[(i-startTime)//3600]+=1
            return freq
        
        elif(freq=="day"):
            c=0
            x=60
            # print(self.tweets[tweetName])
            m = ((endTime-startTime)//86400 )+1
            freq=[0]*m
            for i in sorted(self.tweets[tweetName]):
                if(i>=startTime and i<=endTime):
                    freq[(i-startTime)//86400]+=1
            return freq
                
        
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)