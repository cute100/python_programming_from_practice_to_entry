from pathlib import Path
path=Path('learning_python.txt')
contests=path.read_text().replace('Python','C')

for line in contests.splitlines():
    print(line)

