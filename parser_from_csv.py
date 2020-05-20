import csv
import json

path_r = "delete_many_one_05_08_2019.csv"
path_w_csv = "output.csv"
path_w_txt = "output.txt"
fieldnames_w_1 = ['ding_id', 'flow']
fieldnames_w_2 = ['ding_id']
fieldnames_w_3 = 'all'
fieldnames_w_4 = ['ding_id', 'flow', 'user_ids', 'dt', 'no_key']


def csv_dict_reader(path):
    """
    Read a CSV file using csv.DictReader
    """
    with open(path) as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        data = []
        for line in reader:
            json_line = json.loads(line["json"])
            json_line["dt"] = line["dt"]
            data.append(json_line)
    return data


def get_all_keys(list_dicts):
    list_key = []
    for i in range(0, len(list_dicts)):
        for dict_i in list_dicts[i]:
            if dict_i not in list_key:
                list_key.append(dict_i)
    return list_key


def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    if fieldnames == 'all':
        fieldnames = get_all_keys(data)
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames, restval='no value for key',
                                extrasaction='ignore')
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def txt_writer(path, fieldnames, data):
    """
    Writes a TXT file
    """
    if fieldnames == 'all':
        fieldnames = get_all_keys(data)
    with open(path, "w") as out:
        for row in data:
            data_str = ""
            for i in range(0, len(fieldnames)):
                key = row.get(fieldnames[i])
                if key:
                    data_str = data_str + fieldnames[i] + ' = ' + str(row[fieldnames[i]]) + ', '
                else:
                    data_str = data_str + fieldnames[i] + ' = no value for key, '
            data_str = data_str[:-2]
            out.write(data_str + ' \n')


my_list = csv_dict_reader(path=path_r)
csv_dict_writer(path=path_w_csv, fieldnames=fieldnames_w_1, data=my_list)
txt_writer(path=path_w_txt, fieldnames=fieldnames_w_2, data=my_list)
