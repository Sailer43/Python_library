__main__ = "Queue on linked list"

"""TO_DO"""

import __linked_list__ as ll
class Queue:
    """TO_DO"""

    def __init__(self, data = None):
        self.ref = ll.__linked_list__(data)

    def enqueue(self, data):
        self.ref.add_at_start(self, data)

    def __iter__(self):
        return self.ref.__iter__()
