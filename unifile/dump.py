#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def yml(file_path: str, data: dict, t_encoding: str = "utf-8"):
    """ 
    best for save settings as dictionary to yaml
    """
    import yaml
    try:
        os.remove(file_path)
    except:
        pass
    try:
        with open(file_path, "w", encoding=t_encoding) as yaml_conf:
            yaml.safe_dump(data, yaml_conf)
    except OSError:
        pass


def txt(file_path: str, data: str, line: int = False, t_encoding: str = "utf-8", write_mode: str = "w"):
    """
    if line is number and you give lines as data you can save only 1 line if you want save 10 lines
    for i in range(10):
        unifile.dump.txt("file.txt",lines,i)
    write_mode r or rb default r
    t_encoding default utf-8
    """
    try:
        os.remove(file_path)
    except:
        pass
    try:
        with open(file_path, write_mode, encoding=t_encoding) as t_file:
            if line > 0:
                lines = []
                lines[line] = data
                t_file.writelines(lines)
            else:
                t_file.write(data)
    except FileNotFoundError:
        pass


def excel(file_path: str, data: list, list_of_column_names: list = False, mode: str = "array", t_encoding: str = "utf-8", row_names: list = None):
    """
    array =save multidimensional array
    [["name","sex","age"],["John","male",20]
    list_of_column_names = default is False for no column or list for column names
    excel = save in to excel file
    """
    import pandas as pd

    try:
        os.remove(file_path)
    except:
        pass
    if mode == "array":
        my_list = pd.DataFrame(data)
        my_list.to_csv(file_path, encoding=t_encoding,
                       header=list_of_column_names)
    elif mode == "excel":
        try:
            os.remove(file_path)
        except:
            pass

        e = pd.DataFrame(
            data,
            index=['row 1', 'row 2', 'row 3'],
            columns=list_of_column_names
        )

        e.to_excel(file_path)


def js(file_path: str, data: dict, t_encoding: str = "utf-8"):
    """
    dictionary save to json
    """
    import json
    try:
        os.remove(file_path)
    except:
        pass
    # open the file
    with open(file_path, "w", encoding=t_encoding) as f:
        json.dump(data, f)
