import heapq
import time
class Twitter:

    def __init__(self):
        self.followmap = dict()
        self.postmap = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.postmap:
            self.postmap[userId] = list()
        self.postmap[userId].append((-time.time(), tweetId, userId, len(self.postmap[userId])))
        #heapq.heappush(self.postmap[userId], (-time.time(), tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        news = list()
        followees = list()
        heap = list()

        if userId in self.followmap:
            followees = self.followmap[userId]

        for followee in followees: 
            posts = self.postmap[followee] if followee in self.postmap else []
            # push the most recent post from each follower onto the heap
            if posts:
                heapq.heappush(heap, posts[-1])
        # push your own tweet
        if userId in self.postmap:
            heapq.heappush(heap, self.postmap[userId][-1])
        
        while heap and len(news) < 10:
            # extract the most recent post
            time, most_recent_post, current_user, index = heapq.heappop(heap)
            news.append(most_recent_post)
            if self.postmap[current_user] and index-1 >= 0:
                heapq.heappush(heap, self.postmap[current_user][index-1])
        
        return news
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            self.followmap[followerId] = set()
        if followerId == followeeId:
            return None
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followmap:
            self.followmap[followerId].discard(followeeId)
