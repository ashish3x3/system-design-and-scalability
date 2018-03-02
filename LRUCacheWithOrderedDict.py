
#  https://www.kunxi.org/blog/2014/05/lru-cache-in-python/


import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

In the contrast of the traditional hash table, the get and set operations are both write operation in
LRU cache. The timestamp is mere the order of the operation. So an ordered hash table, aka OrderedDic, might be able to meet our needs. Here is the LRU cache implementation based on OrderedDict:



class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1


We use cache to store the (key, value) mapping, and lru and automatic incremented tm to track the access history, pretty straightforward, right?

python -m cProfile lru-cache-test.py naive-lru-cache

It shows that the significant CPU time, 1.403 out of 1.478 is spent on the min operation, more concretely, this statement:

old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
We naively identify the least-recently-used item by a linear search with time complexity O(n) instead of O(1), a clear violation of the set’s requirement.






from datetime import datetime


class LRUCacheItem(object):
    """Data structure of items stored in cache"""
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.timestamp = datetime.now()


class LRUCache(object):
    """A sample class that implements LRU algorithm"""

    def __init__(self, length, delta=None):
        self.length = length
        self.delta = delta
        self.hash = {}
        self.item_list = []

    def insertItem(self, item):
        """Insert new items to cache"""

        if item.key in self.hash:
            # Move the existing item to the head of item_list.
            item_index = self.item_list.index(item)
            self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index+1:]
            self.item_list.insert(0, item)
        else:
            # Remove the last item if the length of cache exceeds the upper bound.
            if len(self.item_list) > self.length:
                self.removeItem(self.item_list[-1])

            # If this is a new item, just append it to
            # the front of item_list.
            self.hash[item.key] = item
            self.item_list.insert(0, item)

    def removeItem(self, item):
        """Remove those invalid items"""

        del self.hash[item.key]
        del self.item_list[self.item_list.index(item)]

    def validateItem(self):
        """Check if the items are still valid."""

        def _outdated_items():
            now = datetime.now()
            for item in self.item_list:
                time_delta = now - item.timestamp
                if time_delta.seconds > self.delta:
                    yield item
        map(lambda x: self.removeItem(x), _outdated_items())
 test_LRU.py
from lru import *
from time import sleep


def print_cache(cache):
    for i, item in enumerate(cache.item_list):
        print ("index: {0} "
               "key: {1} "
               "item: {2} "
               "timestamp: {3}".format(i,
                                       item.key,
                                       item.item,
                                       item.timestamp))

one = LRUCacheItem(1, 'one')
two = LRUCacheItem(2, 'two')
three = LRUCacheItem(3, 'three')

print "Initial cache items."
cache = LRUCache(length=3, delta=5)
cache.insertItem(one)
cache.insertItem(two)
cache.insertItem(three)
print_cache(cache)
print "#" * 20

print "Insert a existing item: {0}.".format(one.key)
cache.insertItem(one)
print_cache(cache)
print "#" * 20

print "Insert another existing item: {0}.".format(two.key)
cache.insertItem(two)
print_cache(cache)
print "#" * 20

print "Validate items after a period of time"
sleep(6)
cache.validateItem()
print_cache(cache)
print "#" * 20















