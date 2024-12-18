import json


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def compare_missing_entries(base, target):
    for key, value in base.items():
        if key not in target:
            if isinstance(value, dict):
                # Key is missing and value is a dict
                target[key] = {}
                # Recurse into the dictionary to add missing subkeys
                compare_missing_entries(value, target[key])
            else:
                # Key is missing and value is not a dict
                target[key] = value
                print(f"Values to add: {value}")
        else:
            # Key exists in target
            if isinstance(value, dict) and isinstance(target[key], dict):
                # Both values are dictionaries, recurse into them
                compare_missing_entries(value, target[key])
            elif isinstance(value, dict) and not isinstance(target[key], dict):
                # In base it's a dict, but in target it's not
                target[key] = {}
                # Recurse into the dictionary to add missing subkeys
                compare_missing_entries(value, target[key])
            # If the value is not a dictionary, do nothing since the key exists

def main():
    base = load_json('json_delta/en_US.json')
    target = load_json('json_delta/de_DE.json')

    compare_missing_entries(base, target)

    save_json(target, 'json_delta/updated_german.json')

if __name__ == '__main__':
    main()