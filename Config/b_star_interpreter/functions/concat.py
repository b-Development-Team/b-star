def concat(*items: tuple[any]):
    if isinstance(items[0], list):
        valid = all(isinstance(it, list) for it in items)
        if valid:
            return sum(items, [])  # Flattens one level deep

    # make sure all items are strings
    converted_items = map(str, items)
    return "".join(converted_items)
