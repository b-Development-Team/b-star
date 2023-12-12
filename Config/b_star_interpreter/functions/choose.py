import random


def choose(*arr):
    # Check if the first element of arr is a list or tuple
    items = arr[0] if len(arr) == 1 and isinstance(arr[0], (list, tuple)) else arr
    # Get a random index within the range of the items' length
    rand = random.randint(0, len(items) - 1)
    # Return the randomly selected item
    return items[rand]