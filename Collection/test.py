__main__ = "test"

"""test script"""

import __linked_list__

a = [1, 2, 3, 4]
b = __linked_list__.__linked_list__(a, has_next = False, has_previous = True)
for element in b:
    print(element)
