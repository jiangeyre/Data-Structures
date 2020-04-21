class Node(object):
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next_node = next_node
   def __str__(self):
       return f"{self.data} : {self.next_node}"

    def reverse_list(list_head):
	length_index = 0
current_node = list_head
while current_node.next_node != None:
   		length_index += 1
   		current_node = current_node.next_node
while length_index > 0:
   		current_node = list_head
   		index = 0
  		while index != length_index:
       		current_node.data, current_node.next_node.data =\
         			current_node.next_node.data, current_node.data
       		current_node = current_node.next_node
       		index += 1
   		length_index -= 1


def reverse(head):
    list_ptr = head.next_node
    rev_list = head
    rev_list.next_node = None
    while list_ptr != None:
       x = list_ptr
       list_ptr = list_ptr.next_node
       x.next_node = rev_list
       rev_list = x
    return rev_list