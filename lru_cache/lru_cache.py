from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.cache = {}
    self.storage = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache.
  """
  def get(self, key):
    #get key from cache
    node = None
    if key in self.cache:
        node = self.cache[key]
    else:
        return None
    #move node from cache to beginning of DLL queue
    self.storage.delete(node)
    self.storage.add_to_head(node.value, key)
    #return fetched key's value
    return node.value

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply
  want to overwrite the old value associated with the key with
  the newly-specified value.
  """
  def set(self, key, value):
    #if key is already in cache, update it
    if key in self.cache:
        #move node to beginning of list
        self.storage.add_to_head(value, key)
        #save node to add to cache
        node = self.storage.head
        #change cache value to new value
        self.cache[key] = node
    #if cache length is maxed, add new item to head and remove oldest value from tail
    elif len(self.cache) == self.limit:
        #add item to beginning of queue
        self.storage.add_to_head(value, key)
        #save node to add to cache
        node = self.storage.head
        #set in cache
        self.cache[key] = node
        #remove tail node key from cache
        item_to_remove = self.storage.tail

        del self.cache[item_to_remove.key]
        #remove tail
        self.storage.remove_from_tail()
    #else simply add item
    else:
        #add item to beginning of queue
        self.storage.add_to_head(value, key)
        #save node to add to cache
        node = self.storage.head
        #add item to cache
        self.cache[key] = node
