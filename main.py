from pprint import pprint
import csv
import re

with open("C:\\Users\pushk\Desktop\phonebook_raw (1).csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


pattern = r"(\+7|8)*([(\s]+)*(\d{3})([)\s-]+)*(\d{3})[-]*(\d{2})[-]*(\d{2})([\s(]+)*(доб.)*\s*(\d{4})*\)*"
res_tel = r"+7(\3)\5-\6-\7 \9\10"


def numbers(lst: list, pat, template):
    res_list = []
    for cont in lst:
        number = re.sub(pat, template, cont[5])
        fullname = ' '.join(cont[:3]).split(' ')
        final_contact = [fullname[0], fullname[1], fullname[2], cont[3], cont[4], number, cont[6]]
        res_list.append(final_contact)
    return res_list


def get_dict(cont_list: list):
    dictionary = {}
    for cont in cont_list:
        dictionary[cont[0], cont[1]] = []
    return dictionary


def duplicates(contact_list: list, contacts_dict: dict):
    for cont in contact_list:
        val = tuple(cont[0:2])
        for item in cont:
            if item not in contacts_dict[val]:
                ind = cont.index(item)
                contacts_dict[val].insert(ind,item)
    final_list = list(contacts_dict.values())
    return final_list


tel_list = numbers(contacts_list, pattern, res_tel)
cont_dict = get_dict(tel_list)
final_res = duplicates(tel_list, cont_dict)
pprint(final_res)


# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook_res.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_res)
