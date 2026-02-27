import os
from scanner import scan_directory 
from indexer import build_index
from search import run_search

def main():
    print("Local File Search Engine")
    print("Choose a folder to index, then type search queeries.")

    directory_path = input("Enter directory to index: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory. Exiting.")
        return
    
    file_index = scan_directory(directory_path)

    if not file_index:
        print("No files found. Exiting")
        return
    
    inverted_index = build_index(file_index)

    if not inverted_index:
        print("No searchable words found. Exiting")

    while True:
        query_string = input("Search (or type 'exit' to quit): ")
        if query_string == "exit":
            break

        results = run_search(inverted_index, query_string)
        if not results:
            print("No matching files found")
            continue

        for file_path in results:
            print(f"Results:{file_path}")

    print("Goodbye")

if __name__ == "__main__": 
    main()