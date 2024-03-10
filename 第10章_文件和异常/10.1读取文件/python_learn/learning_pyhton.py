from pathlib import Path
path=Path('learning_python.txt')
contests=path.read_text()
print(contests)

lines=contests.splitlines()
for line in lines:
    print(line)

