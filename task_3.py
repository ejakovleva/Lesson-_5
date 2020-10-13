with open("text_3.txt", "r", encoding='utf-8') as salaries:
    salaries_list = salaries.read().split("\n")
    salaries_tuples = []
    for i in salaries_list:
        x = i.split()
        x[1] = float(x[1])
        salaries_tuples.append(tuple(x))

    person_salary_dict = dict(salaries_tuples)
    print(person_salary_dict)

    for i, j in person_salary_dict.items():
        if j < 20000:
            print(f'{i} зарабатывает меньше 20 тыс руб')

    average_salary = sum(person_salary_dict.values())/len(person_salary_dict.keys())
    print(f'Средняя з/пл составляет {round(average_salary, 2)} руб')








