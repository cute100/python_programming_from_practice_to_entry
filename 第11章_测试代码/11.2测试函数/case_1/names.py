from Python编程从入门到实践.第11章_测试代码.case_1.name_function import get_formatted_name
print("Enter 'q' at any time to quit")
while True:
    first=input("\nPlese give me a first name:")
    if first=='q':
        break
    last=input("\nPlese give me a last name:")
    if last=='q':
        break
    formatted_name=get_formatted_name(first,last)
    print(f"\tNeatly formatted name:{formatted_name}")