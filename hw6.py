from typing import List, Tuple, Optional


def bounds(array: List[float], target: [float]) -> Optional[Tuple[int, int]]:
    left, right = left_bound(array, target), right_bound(array, target)
    if left is None or right is None:
        return None
    return (left, right)


def left_bound(array: List[float], target: [float]) -> Optional[int]:
    if not array:
        return None

    lower, upper = 0, len(array)
    while lower < upper:
        mid = (lower + upper) // 2
        if target > array[mid]:
            lower = mid+1
        else:
            upper = mid

    if upper < 0 or lower >= len(array):
        return None
    if array[upper] == target:
        return lower
    return 0


def right_bound(array: List[float], target: [float]) -> Optional[int]:
    if not array:
        return None

    lower, upper = 0, len(array)
    while lower < upper:
        mid = (lower + upper) // 2
        if target >= array[mid]:
            lower = mid+1
        else:
            upper = mid

    if upper <= 0 or lower >= len(array):
        return None
    if array[lower-1] == target:
        return lower-1
    return None


def tests() -> None:
    assert bounds([1.5, 2.3, 2.3, 5.5], 2.3) == (1, 2)
    assert bounds([1.5, 2.3, 2.3, 5.1], 1.5) == (0, 0)
    assert bounds([1.5, 2.3, 2.3, 5.1], 10) is None
    assert bounds([1.5, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 5.1], 2.3) == (1, 7)
