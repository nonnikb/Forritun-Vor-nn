my_dict = {'Average Directory': [228136, 202099, 561775, 100294, 799927, 826594, 569863, 2737508]}

if all_dir not in avg_list:
    avg_list[all_dir] = [avg_size]
else:
    if avg_size not in avg_list:
        avg_list[all_dir] += [avg_size]


        def player_2():
            print("1. Enter a movie title")
            print("2. Give up")
            choice = input("Pick an action:")
            if choice == '2':
                print("\nPlayer 1 wins!")
                quit()
            elif choice == '1':
                title2 = input("Enter a movie title: ")
                return title2
            else:
                print("Invalid input, what would you like to do?")
                player_2()
