def all_thing_is_obj(object: any) -> int:
    """
    Prints the object types and returns 42.
    """
    if (isinstance(object, str)):
        print(f"{object} is in the kitchen : {type(object)}")
    elif (type(object) in [list, tuple, dict, set]):
        print(f"{str(type(object).__name__).capitalize()} : {type(object)}")
    else:
        print("Type not found")
    return 42
