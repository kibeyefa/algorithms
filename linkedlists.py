class Node:
   def __init__(self, value, next_node=None):
      self.value = value
      self.next_node = next_node

class Linked_lists:
   def __init__(self, head):
      self.head = Node(head)
      self.items = [self.head]
      self.item_values = [self.head.value]

   def add_node(self, value, next_node=None):
      new_node = Node(value, next_node)     
      self.items[-1].next_node = new_node
      self.items.append(new_node)
      self.item_values.append(new_node.value)

   def length(self):
      return len(self.items)
      
def is_circular(data):
   return True if data.items[-1].next_node == data.head.value else False