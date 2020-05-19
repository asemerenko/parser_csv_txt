import csv
import json

path_r = "delete_many_one_05_08_2019.csv"
path_w_csv = "output.csv"
path_w_txt = "output.txt"
fieldnames_w_1 = ['ding_id', 'flow']
fieldnames_w_2 = ['ding_id']


def csv_dict_reader(path, fieldnames):
    """
    Read a CSV file using csv.DictReader
    """
    with open(path) as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        data = []
        for line in reader:
            json_line = json.loads(line["json"])
            data_str = "{"
            for i in range(0, len(fieldnames)):
                data_str = data_str + '"'+fieldnames[i]+'": "'+json_line[fieldnames[i]]+'",'
            data_str = data_str[:-1] + '}'
            data_dict = json.loads(data_str)
            data.append(data_dict)
    return data


def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def txt_writer(path, fieldnames, data):
    """
    Writes a TXT file
    """
    with open(path, "w") as out:
        for row in data:
            data_str = ""
            for i in range(0, len(fieldnames)):
                data_str = data_str + fieldnames[i] + ' = ' + row[fieldnames[i]] + ', '
            data_str = data_str[:-2]
            out.write(data_str + ' \n')


my_list = csv_dict_reader(path=path_r, fieldnames=fieldnames_w_1)
csv_dict_writer(path=path_w_csv, fieldnames=fieldnames_w_1, data=my_list)
txt_writer(path=path_w_txt, fieldnames=fieldnames_w_2, data=my_list)
