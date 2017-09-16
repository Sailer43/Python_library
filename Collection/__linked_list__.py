__main__ = "Linked List"

"""TO_DO"""


class __linked_list__:
    """TO_DO"""

    class __node__:
        """TO_DO"""
        
        def __init__(self, data = None):
            self.data = data
            if (__linked_list__.has_next):
                self.post_node = None
            if (__linked_list__.has_previous):
                self.pre_node = None

        def set_data(data):
            self.data = data
                
        def set_post(post_node):
            self.post_node = post_node
            
        def set_pre(pre_node):
            self.pre_node = pre_node
            
    def __init__(self, data : list = None,
                 has_next = True, has_previous = False):
        self.has_next = has_next
        self.has_previous = has_previous
        if (self.has_next and self.has_previous):
            #double linked
            self.first_smart_node = __node__()
            self.last_smart_node = __node__()
            pre_node = self.first_smart_node
            last_node = self.last_smart_node
            pre_node.set_post(last_node)
            last_node.set_pre(pre_node)
            for element in data:
                n = __node__(element)
                pre_node.set_post(n)
                last_node.set_pre(n)
                n.set_post(last_node)
                n.set_pre(pre_node)
                pre_node = n
        elif (self.has_next):
            #backward linked
            self.first_smart_node = self.__node__()
            pre_node = self.first_smart_node
            for element in data:
                n = __node__(element)
                pre_node.set_post(n)
                pre_node = n
        elif (self.has_previous):
            #forward linked
            self.last_smart_node = __node__()
            last_node = self.first_smart_node
            for element in data:
                n = __node__(element)
                n.set_pre(last_node.pre_node)
                last_node.set_pre(n)
        else:
            assert False, """A linked list must be linked, check constructor
                             making either has_next or has_previous is true"""

    def __iter__(self):
        if (self.has_next):
            self.it_pointer = self.first_smart_node.post_node
        else:
            self.it_pointer = self.last_smart_node.pre_node
        return self.it_pointer.data

    def __next__(self):
        if (self.has_next):
            if (self.it_pointer.post_node == None):
                self.it_pointer = None
                raise StopIteration
            else:
                self.it_pointer = self.it_pointer.post_node
        else:
            if (self.it_pointer.pre_node == None):
                self.it_pointer = None
                raise StopIteration
            else:
                self.it_pointer = self.it_pointer.pre_node
        return self.it_pointer.data
