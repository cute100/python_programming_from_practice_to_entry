from pathlib import Path
path=Path('programming.txt')
contents='I love programming.\n'
contents+='I love creating new ganmes.\n'
contents+='I also love working with data.\n'
path.write_text(contents)