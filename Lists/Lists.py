"""
Lists are a collection of data
"""


my_list = [80, 96, 72, 100, 8]
print(my_list)
my_list.append(1000)
print(my_list)
my_list.insert(2, 1000)
print(my_list)
my_list.remove(8)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.sort()
print(my_list)

"""
The provided Python code is performing various operations on a list named `my_list`. 

Initially, `my_list` is defined with five integer elements: `[80, 96, 72, 100, 8]`. This list is then printed to the console with `print(my_list)`.

Next, the `append` method is used to add the integer `1000` to the end of the list. The `append` method in Python adds an element to the end of the list. The updated list is then printed again.

Following this, the `insert` method is used to add another `1000` at the second index of the list (Python uses zero-based indexing). The `insert` method in Python inserts an element at a specific position in the list. The list, now with the newly inserted element, is printed.

The `remove` method is then used to remove the first occurrence of the integer `8` from the list. The `remove` method in Python removes the first occurrence of the specified value. The list, now without the `8`, is printed.

The `pop` method is used next to remove the element at the zeroth index of the list. The `pop` method in Python removes the element at the specified position, or the last item if the index is not specified. The list, now without the first element, is printed.

Finally, the `sort` method is used to sort the elements of the list in ascending order. The `sort` method in Python sorts the elements of a list. The sorted list is then printed.
"""







