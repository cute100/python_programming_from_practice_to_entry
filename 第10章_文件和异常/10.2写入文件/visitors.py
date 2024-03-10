from pathlib import Path

name_text=Path('guest.txt')
name=input('Plese write you name :')
name_text.write_text(name,encoding='gbk')