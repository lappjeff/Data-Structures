class BinarySearchTree:
      def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

      def insert(self, value):
        #handles case where leaf node is found and value is smaller
        if self.left is None and value <= self.value:
            self.left = BinarySearchTree(value)
        #handles case where leaf node is found and right is smaller
        elif self.right is None and value > self.value:
            self.right = BinarySearchTree(value)
        #repeats first two checks for left node
        elif value <= self.value:
            self.left.insert(value)
        #repeats first two checks for right node
        elif value > self.value:
            self.right.insert(value)


      def contains(self, target):
          if self.value == target:
              return True
          if target > self.value and self.right is not None:
              return self.right.contains(target)
          elif target <= self.value and self.left is not None:
              return self.left.contains(target)
          else:
              return False


      def get_max(self):
        #simply goes to far right node and returns value
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

      def for_each(self, cb):
          #calling callback on value
          cb(self.value)

          #base case
          if not self.left and not self.right:
              return
          #if node has a left and a right recursively go through them
          elif self.left and self.right:
              self.left.for_each(cb)
              self.right.for_each(cb)
          #if just a left node recursively call through it
          elif self.left:
              self.left.for_each(cb)
          #if just a right node recursively call through it
          elif self.right:
              self.right.for_each(cb)
