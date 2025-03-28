def analyzer(payload):

    if isinstance(payload, dict):
        clone_dict = {}
        for key, value in payload.items():
            clone_dict[key] = analyzer(value)
        return clone_dict

    elif isinstance(payload, list) and payload:
        return [analyzer(payload[0])]

    else:
        return type(payload).__name__


if __name__ == "__main__":
    x = {"a": 1, "b": {"c": True}}
    analyzer(x)
