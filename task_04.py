def sort_list(collection):
    if not collection:
        return
    min_item = min(collection)
    max_item = max(collection)
    for i in range(len(collection)):
        if collection[i] == min_item:
            collection[i] = max_item
        elif collection[i] == max_item:
            collection[i] = min_item
    collection.append(min_item)
