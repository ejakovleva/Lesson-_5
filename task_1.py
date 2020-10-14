with open("user_data_1.txt", "w+", encoding="utf-8") as user:
    x = [input("Enter your personal data: "), '\n']
    while True:
        x.append(f'{input("")}')
        if "" in x:
            break
        x.append('\n')
    user.writelines(x)

with open("user_data_1.txt", "r+", encoding="utf-8") as user:
    print(user.readlines())
    print(user.tell())

