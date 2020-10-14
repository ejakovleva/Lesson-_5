with open('user_data_1.txt', 'r+', encoding="utf-8") as user_file:
    x = user_file.readlines()
    print(f"The 'user_data_1.txt' file has {len(x)} strings")
    for i, j in enumerate(x):
        words = j.split()
        print(f'The string №{i+1} has {len(words)} words')

