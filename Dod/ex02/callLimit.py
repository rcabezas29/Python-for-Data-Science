def callLimit(limit: int):
    """Decorator that limits the number of executions to a function"""
    count = 0

    def callLimiter(function):
        """Wrapper function"""

        def limit_function(*args: any, **kwds: any):
            """Uses a nonlocal variable count to keep track of how
            many times the decorated function has been called"""
            nonlocal count
            try:
                assert count < limit, f"{function} call too many times"
                count += 1
                function(*args, **kwds)
            except AssertionError as msg:
                print(f"Error: {msg}")

        return limit_function

    return callLimiter
