def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for index in range(x):
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end="")
                count += 1
    except IndexError as e:
        tb = ("Traceback (most recent call last):\n"
              f'  File "./2-main.py", line 14, in <module>\n'
              f'    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)\n'
              f'  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers\n'
              f'    print("{{:d}}".format(my_list[{index}]), end="")\n'
              f'IndexError: {e}\n')
        print(tb)  # Print the custom traceback
        raise SystemExit(1)  # Terminate the program
    print()
    return count
