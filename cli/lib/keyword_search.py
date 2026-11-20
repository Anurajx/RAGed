from lib.search_utils import load_dataset


def search_logic(query , limit):
    # print(f"QUERY {query}")
    dataset = load_dataset()
    # print(f"DATASET {dataset}")
    formattedQuery = query.lower().translate({ord('!'): None, ord('.'): None, ord(','): None, ord('-'): None})
    result = []
    for movie in dataset:
        formattedMovie = movie["title"].lower().translate({ord('!'): None, ord('.'): None, ord('-'): None})
        if formattedQuery in formattedMovie:
            # print(movie["title"])
            result.append(movie["title"])

        if len(result) == limit:
            break

    return result
