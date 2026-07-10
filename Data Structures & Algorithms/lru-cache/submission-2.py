class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    # doubly ll and a map -- go with this
    # or a min heap and a map?

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.lrumap = {}

    def get(self, key: int) -> int:
        # move the node to front of the list
        # return the value
        # if value is not there, return -1
        if key in self.lrumap:            
            node = self.lrumap[key]
            if node == self.head:
                # do no moving around
                return self.lrumap[key].val
            
            if node == self.tail:
                self.tail = self.tail.prev
            
            # if node in middle or last, move to front
            next = node.next
            prev = node.prev
            # re-attach nodes in between the removed node
            if prev:
                prev.next = next
            if next:
                next.prev = prev
            
            # put the node in front
            node.prev = None
            node.next = self.head
            self.head.prev = node

            # re-adjust head
            self.head = node

            return self.lrumap[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        # insert node to front of list if new
        # if exists, update val, move node to front of list
        # if total count > capacity, remove last node

        if key in self.lrumap:
            # update value
            node = self.lrumap[key]
            node.val = value

            # if in front, do nothing, just return
            if self.head == node:
                return None

            if node == self.tail:
                self.tail = self.tail.prev

            # if node in middle or last, move to front
            next = node.next
            prev = node.prev
            # re-attach nodes in between the removed node
            if prev:
                prev.next = next
            if next:
                next.prev = prev
            
            # put the node in front
            node.prev = None
            node.next = self.head
            self.head.prev = node

            # re-adjust head
            self.head = node

        else:
            node = Node(key, value)
            node.next = self.head
            node.prev = None
            
            if self.head:
                self.head.prev = node

            self.head = node
            if not self.tail:
                self.tail = node

            self.lrumap[key] = node
        
        # if capacity exceeded
        if len(self.lrumap) > self.capacity:
            del self.lrumap[self.tail.key]
            
            prev = self.tail.prev
            self.tail.prev = None
            prev.next = None
            self.tail = prev
            






        
