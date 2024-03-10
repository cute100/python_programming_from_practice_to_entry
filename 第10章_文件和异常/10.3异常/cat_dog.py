from pathlib import Path

file_names=["cat_and_dog\cat.txt","cat_and_dog\dog.txt"]

for file_name in file_names:
    try:
        path=Path(file_name)
        names=path.read_text()
        print(f"{names}\n")
    except FileNotFoundError:
        pass