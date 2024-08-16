def connect_dicts(dict1, dict2):
    prioritet_dict = dict1 if sum(dict1.values()) > sum(dict2.values()) else dict2
    if dict1 is prioritet_dict:
        result = {**dict2, **dict1}
    else:
        result = {**dict1, **dict2}
    result = {key: val for key, val in result.items() if val >= 10}

    return dict(sorted(result.items(), key=lambda x: x[1]))
