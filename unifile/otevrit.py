#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def yml(file_path: str, t_encoding: str = "utf-8"):
    """ 
    best for open your saved settings
    :return:
    dictionary

    """
    import yaml
    try:
        with open(file_path, "r", encoding=t_encoding) as yaml_conf:
            yaml_file: dict = yaml.safe_load(yaml_conf)
        return yaml_file
    except OSError:
        print("FileNotFoundError")


def txt(file_path: str, line: int = False, t_encoding: str = "utf-8", read_mode: str = "r"):
    """
    read_mode r or rb default r
    t_encoding default utf-8
    return file object or line if line=1
    for more line cal 
    for i in range(10):
        txt("file.txt",line=i)
    """
    try:
        with open(file_path, read_mode, encoding=t_encoding) as t_file:
            if line > 0:
                lines = t_file.readlines()
                return lines[line]
            else:
                return t_file.read()
    except FileNotFoundError:
        print("FileNotFoundError")


def excel(file_path: str, mode: str = "array", header: list = None, t_encoding: str = "utf-8", **kwargs):
    """
    mode array = multidimensional array
    [["name","sex","age"],["John","male",20]]
    mode str = load as string
        optional param is deli ="|"  | is delimeter
    mode panda load pandas data frame
    mode dictionary = coming soon


    TODO: mode mark = for opening csv file like this(markdown syntax)
    |name|sex |age|
    |----|----|---|
    |John|male|20 |
    """
    import csv
    import pandas as pd
    # https://docs.python.org/3/library/csv.html
    if mode == "mark":
        pass
    elif mode == "array":
        try:
            with open(file_path, "r",  encoding=t_encoding) as csv_file:
                csv_output = csv.reader(csv_file)

                arr = []

                for row in csv_output:
                    arr.append(row)

                return arr
        except FileNotFoundError:
            print("FileNotFoundError")
    elif mode == "str":
        deli = kwargs.get("deli") if kwargs.get("deli") != None else ","
        try:
            with open(file_path, "r",  encoding=t_encoding) as csv_file:
                csv_output = csv.reader(csv_file)

                a = ""
                for row in csv_output:
                    a += ','.join(row)
                    a += "\n"

                a = a.replace(",", deli)

                return a
        except FileNotFoundError:
            print("FileNotFoundError")
    elif mode == "panda":
        try:
            c = pd.read_csv(file_path, header,
                            encoding=t_encoding, engine='python')
            return c
        except FileNotFoundError:
            print("FileNotFoundError")
    else:
        pass


def js(file_path: str, t_encoding: str = "utf-8"):
    """
    if file_path is url can load data too
    :return:
    dictionary
    """
    import json

    def getResponse(url):
        import urllib.request
        operUrl = urllib.request.urlopen(url)
        if(operUrl.getcode() == 200):
            data = operUrl.read()
            jsonData = json.loads(data)
        else:
            print("Error receiving data", operUrl.getcode())
        return jsonData

    if file_path.startswith("http"):
        return getResponse(file_path)
    else:
        # open the file
        with open(file_path, "r", encoding=t_encoding) as f:
            data = json.load(f)
        return data


def pdf(file_path: str):
    """
    extract data from pdf
    :return:
    string
    """
    # importing required modules
    import PyPDF2

    try:
        with open(file_path, mode='rb') as f:
            reader = PyPDF2.PdfFileReader(f)

            a = ""

            for page in reader.pages:
                a += page.extractText()

        return a
    except FileNotFoundError:
        print("FileNotFoundError")
