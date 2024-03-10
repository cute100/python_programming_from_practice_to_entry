print("Give me two numbers,and I'll divide them")
print("Enter 'q' to quit")
while True:
    first_number=input("\nFirst number:")
    if first_number=="q":
        break
    scend_number=input("Second number:")
    if scend_number=="q":
        break
    try:
        answer=int(first_number)/int(scend_number)
    except ZeroDivisionError:
        print("You can't divide by0!")
    else:
        print(answer)