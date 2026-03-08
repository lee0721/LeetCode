class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxheap = []
        sources = set(self.follows[userId])
        sources.add(userId)
        for uid in sources:
            arr = self.tweets[uid]
            if arr:
                idx = len(arr) - 1
                t, tid = arr[idx]
                heapq.heappush(maxheap, (-t, tid, uid, idx))
        
        while maxheap and len(res) < 10:
            neg_t, tid, uid, idx = heapq.heappop(maxheap)
            res.append(tid)
            idx -= 1
            if idx >= 0:
                t2, tid2 = self.tweets[uid][idx]
                heapq.heappush(maxheap, (-t2, tid2, uid, idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)