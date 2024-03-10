from pathlib import Path
import os
def count_words(path):
    """计算一个文件大概包括多少个单词"""
    path=Path(path)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry,the file {path} does not exist.")
    else:
        """计算文件大致包括多少个单词"""
        # words = contents.split()
        # num_words = len(words)
        # print(f"The file {path} has about {num_words} words")
        """计算每个文件中1有多少个"""
        one_nums=contents.count('1')
        print(f"The file {path} has about {one_nums} noe")

def files(file_path):
    file_name=os.listdir(file_path)
    return file_name

file_path=r'texts'
file_lists=os.listdir(file_path)
for file in file_lists:
    count_words(f"{file_path}/{file}")
path=Path("alice.txt")

