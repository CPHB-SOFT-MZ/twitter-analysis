from pymongo import MongoClient
from bson.son import SON
from bson.regex import Regex
import re

class TwitterAnalysis():
    def __init__(self):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client.social_net
        self._collection = self._db.tweets_big


    # 1. How many Twitter users are in the database?
    def number_of_users(self):
        return len(self._collection.find({}).distinct("user"))

    # 2. Which Twitter users link the most to other Twitter users? (Provide the top ten.)
    def users_mentioning_others_most(self):
        pattern = re.compile("(?<=^|(?<=[^a-zA-Z0-9-_\\.]))@([A-Za-z]+[A-Za-z0-9_]+)")
        regex = Regex.from_native(pattern)
        pipeline = [
            {"$match": {"text":  {"$regex": regex}}},
            {"$group": {"_id":"$user", "count": {"$sum": 1}}},
            {"$sort": SON([("count", -1)])},
            {"$limit": 10}
        ]

        return self._collection.aggregate(pipeline, allowDiskUse=True)

    # 3. Who are are the most mentioned Twitter users? (Provide the top five.)
    # This is not yet implemented
    def most_mentioned_users(self):
        pattern = re.compile("(?<=^|(?<=[^a-zA-Z0-9-_\\.]))@([A-Za-z]+[A-Za-z0-9_]+)")
        regex = Regex.from_native(pattern)

        pipeline = [
            {"$match": {"text": {"$regex": regex}}},
            {"$project": {"user": "$user", "texts": {"$split": ["$text", " "]}}},
            {"$unwind": "$texts"},
            {"$match": {"texts": {"$regex": regex}}},
            {"$group": {"_id": "$texts", "count": {"$sum": 1}}},
            {"$sort": SON([("count", -1)])},
            {"$limit": 10}
        ]
        return self._collection.aggregate(pipeline, allowDiskUse=True)

    # 4. Who are the most active Twitter users (top ten)?
    def top_ten_active_users(self):
        pipeline = [
            {"$group": {"_id": "$user", "count": {"$sum": 1}}},
            {"$sort": SON([("count", -1)])},
            {"$limit": 10}
        ]
        return self._collection.aggregate(pipeline, allowDiskUse=True)


    # Who are the five most grumpy (most negative tweets) and the most happy
    # (most positive tweets)? (Provide five users for each group)
    def most_grumpy_users(self):
        pipeline = [
            {"$match": {"polarity": {"$eq": 0}}},
            {"$group": {"_id": "$user", "count": {"$sum": 1}}},
            {"$sort": SON([("count", -1)])},
            {"$limit": 5}
        ]
        return self._collection.aggregate(pipeline, allowDiskUse=True)

    def most_happy_users(self):
        pipeline = [
            {"$match": {"polarity": {"$eq": 4}}},
            {"$group": {"_id": "$user", "count": {"$sum": 1}}},
            {"$sort": SON([("count", -1)])},
            {"$limit": 5}
        ]
        return self._collection.aggregate(pipeline, allowDiskUse=True)






