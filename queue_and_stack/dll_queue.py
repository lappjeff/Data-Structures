import sys
from doubly_linked_list import DoublyLinkedList

# enqueue should add an item to the back of the queue.
# dequeue should remove and return an item from the front of the queue.
# len returns the number of items in the queue.

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    self.storage.add_to_tail(value)
    self.size = self.storage.length

  def dequeue(self):
    if self.size > 0:
        item_removed = self.storage.remove_from_head()
        self.size = self.storage.length
        return item_removed
    else:
        return None

  def len(self):
    return self.storage.length
