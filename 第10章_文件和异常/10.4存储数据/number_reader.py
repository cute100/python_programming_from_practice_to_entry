from pathlib import Path
import json

numbers=[2,3,5,7,11,13]

path=Path('numbers.json')
contents=path.read_text()
numbers=json.loads(contents)

print(numbers)