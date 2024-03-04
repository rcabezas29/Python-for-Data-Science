def NULL_not_found(object: any) -> int:
    NoneType = type(None)
    types = {
        NoneType: "Nothing",
        float: "Cheese",
        int: "Zero",
        str: "Empty",
        bool: "Fake"
    }
    if (type(object) in types) and not object or not object == object:
        print(f"{types[type(object)]}: {object} {type(object)}")
        return 0
    else:
        print("Type not found")
        return 1
