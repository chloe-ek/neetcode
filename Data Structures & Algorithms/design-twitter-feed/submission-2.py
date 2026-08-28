class Twitter:

    def __init__(self):
        self.user_followees = defaultdict(set) #  {1: {2}}

        self.user_tweets = defaultdict(list) # {1: [(0, 10)], 2: [(1, 20)]}
        self.order_count = 0
        
        # ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1]]


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.order_count,tweetId))
        self.order_count += 1
            

    def getNewsFeed(self, userId: int) -> List[int]:
        follower_check = set(self.user_followees[userId])
        follower_check.add(userId) # ( 1, 2)

        feeds = []

        for follower in follower_check:
            feeds.extend(self.user_tweets[follower])

        recent_feeds = sorted(feeds, reverse=True)[:10]

        return [tweetid for num, tweetid in recent_feeds]
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followees[followerId].discard(followeeId)
        
