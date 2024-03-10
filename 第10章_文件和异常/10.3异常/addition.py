while True:
    try:
        first_number=input(f"Plese write first_number:")
        if first_number=='q':
            break
        first_number=int(first_number)
        scend_number=input(f"Plese write scend_number:")
        if scend_number == 'q':
            break
        scend_number=int(scend_number)
    except ValueError:
        print("请输入数字！！！")
    else:
        add_result=first_number+scend_number
        print(f"{first_number}+{scend_number}={add_result}")