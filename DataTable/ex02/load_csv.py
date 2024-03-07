import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Takes a path as argument, writes the dimensions of
    the data set and returns it.
    Handles the error cases and return None
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print("File not Found")
        return None
    except pd.errors.EmptyDataError:
        print("EmptyDataError: No columns to parse from file")
        return None
    except PermissionError:
        print(f"Permission denied: '{path}'")
        return None
