import json
from datetime import date
import tkinter as tk
from tkinter import simpledialog, messagebox

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def main():
    data = load_json('json_list/list.json')
    today = date.today()
    today = today.strftime('%Y-%m-%d') 
    print(today)
    for item in data:
        #print(item['ID'], item['Status'],  item['Fälligkeitsdatum'])
        if item['Fälligkeitsdatum'] == today:

            print(f'''Die Berechtigung von {item['User']} wird entfernt!''')
            data.remove(item)

    # save_json(data, 'json_list/list_updated.json')


if __name__ == '__main__':
    main()