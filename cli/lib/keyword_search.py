

def search_logic(query , dataset):
    for i in dataset:
        if query in dataset:
            print(i)
