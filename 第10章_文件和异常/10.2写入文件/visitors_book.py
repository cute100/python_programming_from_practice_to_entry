from pathlib import Path

name_text=Path('guest_book.txt')
guest_names=[]
while True:
    name=input('Plese write you name :')
    if name=='quit':
        break
    guest_names.append(name)
file_string=''
for name in guest_names:
    file_string+=f'{name}\n'
name_text.write_text(file_string,encoding='gbk')