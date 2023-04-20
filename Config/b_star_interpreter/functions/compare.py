# TODO: Inspect types further
def comparevals(v1: float, operator: str, v2: float):
    if operator == ">":
        return v1 > v2
    elif operator == "<":
        return v1 < v2
    elif operator == ">=":
        return v1 >= v2
    elif operator == "<=":
        return v1 <= v2
    elif operator in {"=", "=="}:
        return v1 == v2
    elif operator == "!=":
        return v1 != v2


def compare(v1: float, operator: str, v2: float):
    return 1 if comparevals(v1, operator, v2) else 0
