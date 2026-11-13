import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# print("hi")
def load_dataset():
    # print(BASE_DIR)
    file_path = BASE_DIR / "data" / "movies.json"
    with open(file_path,"r") as f:
        data= json.load(f)

    return data["movies"]

    # movie_names= []
    # for i in data:
    #     for j in range(len(data[i])):
    #         value = data[i]
    #         # print(f"{j}. {value[j]["title"]}")
    #         movie_names.append(value)
    #         # if j==5:
    #         #     break
    # return movie_names

print(load_dataset())
