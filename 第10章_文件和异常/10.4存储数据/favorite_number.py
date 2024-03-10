import json
from pathlib import Path
path=Path(f'favorite_number.json')

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f'你喜欢的数字是{favorite_number}')
else:
    contents=input(f'请输入你喜欢的数字：')
    favorite_number=json.dumps(contents)
    path.write_text(favorite_number)

