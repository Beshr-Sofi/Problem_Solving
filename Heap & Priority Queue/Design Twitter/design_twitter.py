import heapq
from typing import List

class Twitter:
  """
  Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
  and is able to see the 10 most recent tweets in the user's news feed.
  
  Approach:
  - We maintain a global `time` counter to track the chronological order of tweets.
  - We use a dictionary `tweets` mapping a userId to a list of their tweets: (negated_time, tweetId).
    We negate the time so that Python's default Min-Heap acts as a Max-Heap (most recent first).
  - We use a dictionary `following` mapping a userId to a set of userIds they follow.
  - For the news feed, we gather all tweets from the user and their followees, heapify them,
    and extract the 10 smallest elements (which represent the 10 most recent tweets).
  """

  def __init__(self):
    self.tweets = {}
    self.following = {}
    self.time = 0

  def postTweet(self, userId: int, tweetId: int) -> None:
    """
    Compose a new tweet. Time Complexity: O(1)
    """
    if not self.tweets.get(userId):
      self.tweets[userId] = []
    self.tweets[userId].append((-self.time, tweetId))
    self.time += 1

  def getNewsFeed(self, userId: int) -> List[int]:
    """
    Retrieve the 10 most recent tweet ids in the user's news feed.
    Time Complexity: O(T + 10 log T) where T is the total number of tweets by the user and their followees.
    Space Complexity: O(T) to store the combined list of tweets before heapifying.
    """
    temp = list(self.tweets.get(userId, []))
    res = []
    for i in self.following.get(userId, set()):
      if i != userId:
        temp.extend(self.tweets.get(i, []))
    heapq.heapify(temp)
    n = 10 if len(temp) > 10 else len(temp)
    for i in range(n):
      res.append(heapq.heappop(temp)[1])
    return res

  def follow(self, followerId: int, followeeId: int) -> None:
    """
    Follower follows a followee. Time Complexity: O(1)
    """
    if not self.following.get(followerId):
      self.following[followerId] = set()
    self.following[followerId].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    """
    Follower unfollows a followee. Time Complexity: O(1)
    """
    if followerId in self.following and followeeId in self.following[followerId]:
      self.following[followerId].remove(followeeId)

def main():
  obj = Twitter()
  obj.postTweet(1, 5)
  print(obj.getNewsFeed(1))
  obj.follow(1, 2)
  obj.postTweet(2, 6)
  print(obj.getNewsFeed(1))
  obj.unfollow(1, 2)
  print(obj.getNewsFeed(1))

if __name__ == "__main__":
  main()
