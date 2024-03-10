from pathlib import Path

path=Path(f'text_files\pi_digits.txt')
contents=path.read_text().rstrip()
contents.rstrip()
print(contents)
lines=contents.splitlines()
for line in lines:
    print(line)