with open('text_7.txt', 'r', encoding='utf-8') as text_7:
    companies_list = text_7.read().split('\n')
    companies_dict = {}
    for i in companies_list:
        values = i.split()[1:]
        keys = i.split()[0]
        companies_dict.update({keys: values})

    for j in companies_dict:
        companies_dict[j][1] = float(companies_dict[j][1]) - float(companies_dict[j][2])
        companies_dict[j] = companies_dict[j][1]

    companies_list = [companies_dict]
    avg = [i for i in companies_dict.values() if i >= 0]
    average_sum = sum(avg)/len(avg)
    companies_list.append(dict(average_profit=average_sum))
    print(companies_list)

    import json
    with open('text_77.json', 'w') as companies_profit:
        json.dump(companies_list, companies_profit)



