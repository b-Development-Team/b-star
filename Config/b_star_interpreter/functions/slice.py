# TODO: Inspect types further (index_step)
def slice_func(array: list, index_start: int, index_end: int, index_step: float):
    index_step = 1 if index_step is None else int(index_step)
    index_end = "" if index_end is None or index_end == "" else index_end
    index_start = "" if index_start is None or index_start == "" else index_start
    return array[index_start:index_end:index_step]
