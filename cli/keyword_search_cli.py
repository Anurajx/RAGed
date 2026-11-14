import argparse

from lib.keyword_search import search_logic
from lib.search_utils import load_dataset


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print(f"Searching for: {search_parser}")
            # movie_names = load_dataset()
            # print(movie_names)
            results = search_logic(args.query,5)
            print("RESULTS OF SEARCH ARE -> ")
            for i in range(len(results)):
                print(f"{i+1} - {results[i]}")
            # search_logic(, movie_names)

            # print the search query here
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
