def count_in_list(lst: list, s: str) -> int:
    """
    Counts and return the number of 's' present in 'lst'
    """
    return len([e for e in lst if e == s])
