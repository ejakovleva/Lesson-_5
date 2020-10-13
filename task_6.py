with open("text_6.txt", 'r', encoding='utf-8') as text_6:
    subjects_list_1 = text_6.read().split('\n')
    print(subjects_list_1)

    subjects_list_2 = [tuple(i.replace("-", "").split(':')) for i in subjects_list_1]
    subjects_dict = dict(subjects_list_2)
    for i, j in subjects_dict.items():
        subjects_dict[i] = j.replace(" ", '')
        for a in subjects_dict[i]:
            if ord(a) in range(ord('а'), ord('я')):
                subjects_dict[i] = subjects_dict[i].replace(a, '')
            elif ord(a) == 40 or ord(a) == 41:
                subjects_dict[i] = subjects_dict[i].replace(a, ' ')
        subjects_dict[i] = subjects_dict[i].split()
        for a, b in enumerate(subjects_dict[i]):
            subjects_dict[i][a] = int(subjects_dict[i][a])
        subjects_dict[i] = sum(subjects_dict[i])

    print(subjects_dict)

# import re
# s2 = '30(пр)'
# print(re.sub(r'\(.*\)', '', s2))
