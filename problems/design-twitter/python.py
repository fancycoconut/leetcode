class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.tweets.get(userId, [])
        temp = copy.deepcopy(tweets)

        # Get tweets from followers
        followers = self.users.get(userId, [])
        for follower in followers:
            followerTweets = self.tweets.get(follower, [])
            temp.extend(followerTweets)

        sortedTweets = sorted(temp, key=lambda tup: tup[0], reverse=True)

        output = []
        uniqueTweets = set()
        length = min(len(sortedTweets), 10)
        for i in range(length):
            if sortedTweets[i][1] in uniqueTweets:
                continue

            output.append(sortedTweets[i][1])
            uniqueTweets.add(sortedTweets[i][1])

        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            raise Exception("You cannot follow youself")
        if followerId not in self.users:
            self.users[followerId] = []
        self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            raise Exception("You cannot unfollow youself")
        if followerId not in self.users:
            self.users[followerId] = []
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)