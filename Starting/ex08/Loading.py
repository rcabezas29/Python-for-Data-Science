def ft_tqdm(lst: range) -> None:
    """
    ft_tqdm recreates the tqdm function.
    It creates a loading bar when it is iterating over an range of numbers.
    """
    bar = ""
    for i in lst:
        perc = ((i - lst.start) / len(lst) * 100).__round__()
        if perc % 2 == 0:
            bar = "=" * (perc / 2).__round__() + ">"
        print(
            """
            [{:3.0f}%][{: <50}] {}/{}
            """
            .format(perc + 1, bar, (i - lst.start) + 1, len(lst)), end='\r')
        yield i
