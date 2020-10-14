with open('text_4.txt', 'r', encoding='utf-8') as numbers:
    eng_num_list = numbers.read().split("\n")
    from googletrans import Translator
    rus_num_list = []
    for i in eng_num_list:
        translator = Translator()
        z = translator.translate(i, src='en', dest='ru')
        rus_num_list.append(z.text + "\n")
    print(rus_num_list)

with open('text_4_new.txt', 'w', encoding='utf-8') as rus_numbers:
    rus_numbers.writelines(rus_num_list)







