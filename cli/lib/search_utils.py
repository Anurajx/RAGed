import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def load_dataset():
    # print(BASE_DIR)
    file_path = BASE_DIR / "data" / "movies.json"
    with open(file_path,"r") as f:
        data= json.load(f)

    for i in data:
        for j in range(len(data[i])):
            value = data[i]
            print(f"{j}. {value[j]["title"]}")

load_dataset()
