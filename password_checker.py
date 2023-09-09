def pass_word(password):
    new_data = tuple(password)
    new_info = list(new_data)
    maximum = 8
    main_caps = []
    count = 0
    for x in new_info:
        caps_lock = x.upper()
        new_list = main_caps.append(caps_lock)
    all_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ";", ","]
    for v in new_info:
        if v not in all_characters:
            print("Your password is not strong enough, use special characters")
        elif v not in main_caps:
            print("You need to have atleast one Capital letter")
        for x in new_info:
            count = count + 1
        elif count < maximum:
            print("Your password needs to be atleast 8 characters")
        elif all_characters and main_caps in new_info:
            print("You have a strong password")

new_password = input("Enter your Password: ")

pass_word(new_password)

