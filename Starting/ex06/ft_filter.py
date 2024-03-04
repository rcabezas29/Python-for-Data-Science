def ft_filter(f, it) -> object:
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """
    ret = []
    for i in it:
        if f(i):
            ret.append(i)
    return ret
