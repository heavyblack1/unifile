#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This file content examples how to use this module
is for saving and loading many file formats 
Terminology
otevrit is for open 
dump is for save content to file

"""
# for import whole module
import unifile
# or you can import only what you need
from unifile.otevrit import yml as ymlo
from unifile.dump import yml as ymls

import os


# write and save data to yaml
print("################################\nYaml:\n################################")

# your settings what you need save
settings = {
    "network": {
        "port": 22
    },
    "more_settings": True
}

# saving settings
unifile.dump.yml("file.yaml", settings)

# load settings
b = unifile.otevrit.yml("file.yaml")
# print settings
print(b)
# load settings to your program an you ca use later

port = b["network"]["port"]
more_settings = b["more_settings"]

# prints vars
print("Port: " + str(port))
print("more settings " + str(more_settings))


# load and save text to txt file
print("################################\nFile:\n################################")
# \ is for escaping first blank line
my_text = """\
My text
lorem ipsum
"""
# save text
unifile.dump.txt("file.txt", my_text)
# and load and print
print(unifile.otevrit.txt("file.txt"))


# Load data from csv more at: https://en.wikipedia.org/wiki/Comma-separated_values
print("################################\nCSV:\n################################")

# load in array mode
"""
os.path.join() is func for multiplatform path
https://www.geeksforgeeks.org/python-os-path-join-method/
https://docs.python.org/3/library/os.path.html
"""
c = unifile.otevrit.excel(os.path.join("sample", "Import_User_Sample_en.csv"))
print(c)

# Load as str
print("\n# str mode\n")
aa = unifile.otevrit.excel(os.path.join(
    "sample", "Import_User_Sample_en.csv"), "str")
print(aa)

print("\n# str mode with delimeter\n")
ii = unifile.otevrit.excel(os.path.join(
    "sample", "Import_User_Sample_en.csv"), "str", deli="|")
print(ii)

print("\n# panda mode\n")
uu = unifile.otevrit.excel(os.path.join(
    "sample", "Import_User_Sample_en.csv"), "panda")
print(uu)

# save to csv

# data to save
my_list = [
    ["jana", "female", "15"],
    ["adam", "male", "85"],
    ["novak", "male", "57"]
]
list_of_column_names = ["name", "sex", "age"]
# save data with column names
unifile.dump.excel("file.csv", my_list, list_of_column_names)

# save to excel
my_list = [
    ["jana", "female", "15"],
    ["adam", "male", "85"],
    ["novak", "male", "57"]
]
list_of_column_names = ["name", "sex", "age"]

row_names = ['row 1', 'row 2', 'row 3']
# save data with column names
unifile.dump.excel("file.xlsx", my_list, list_of_column_names,
                   "excel", row_names=row_names)


# savedata json or load from url
print("################################\nJson:\n################################")

# json example
urlData = "http://vocab.nic.in/rest.php/states/json"
jsonData = unifile.otevrit.js(urlData)
# print the state id and state name corresponding
for i in jsonData["states"]:
    print(
        f'State Name:  {i["state"]["state_name"]} , State ID : {i["state"]["state_id"]}')

# json loacal file save
d = {"a": "adsd", "time": {"adaa": "yhsyhs"}}

unifile.dump.js("file.json", d)


# PDF
print("################################\nPdf:\n################################")
# load text from pdf file
print(unifile.otevrit.pdf(os.path.join("sample", "sample.pdf")))
