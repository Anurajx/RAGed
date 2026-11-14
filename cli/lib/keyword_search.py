from lib.search_utils import load_dataset


def search_logic(query , limit):
    # print(f"QUERY {query}")
    dataset = load_dataset()
    # print(f"DATASET {dataset}")
    result = []
    for movie in dataset:
        if query in movie["title"].lower():
            # print(movie["title"])
            result.append(movie["title"])

        if len(result) == limit:
            break

    return result
