def ft_statistics(*args, **kwargs) -> None:
    """
    Takes in *args a quantity of unknown number and make the Mean, Median,
    Quartile (25% and 75%), Standard Deviation and Variance according to the
    **kwargs ask.
    """

    def mean(nums):
        """
        Mean of the arguments
        """
        sum = 0
        for val in nums:
            sum += val
        return sum / len(nums)

    def median(nums):
        """
        Median of the arguments
        """
        nums.sort()
        if len(nums) % 2 == 0:
            return nums[round(len(nums) / 2)] + \
                nums[round(len(nums) / 2) + 1] / 2
        else:
            return nums[round(len(nums) / 2) + 1]

    def quartiles(nums):
        """
        25% and 75% quartiles of the arguments
        """
        nums.sort()
        ret = []
        ret.append(nums[round(len(nums) / 4)])
        ret.append(nums[round(len(nums) / 4) * 3])
        return ret

    def standard_deviation(nums):
        """
        Standard deviation of the arguments
        """
        return variance(nums)**(1/2)

    def variance(nums):
        """
        Variance of the arguments
        """
        m = mean(nums)
        size = len(nums)
        sum = 0
        for val in nums:
            sum += (val - m)**2
        return sum / (size - 1)

    nums = [i for i in args]
    try:
        assert len(nums) > 0, "Error - Empty list"
        for x in nums:
            assert isinstance(x, float) or isinstance(x, int), \
                "Invalid argument"
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return

    for k in kwargs:
        if kwargs[k] == "mean":
            print(f"mean: {mean(nums)}")
        elif kwargs[k] == "median":
            print(f"median: {median(nums)}")
        elif kwargs[k] == "quartile":
            print(f"quartile: {quartiles(nums)}")
        elif kwargs[k] == "std":
            print(f"std: {standard_deviation(nums)}")
        elif kwargs[k] == "var":
            print(f"var: {variance(nums)}")
        else:
            continue
