import unittest
import json
from main import compare_missing_entries


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def compare_json_structures(json1, json2, path=""):
    if type(json1) != type(json2):
        return [f"Type mismatch at {path}: {type(json1).__name__} != {type(json2).__name__}"]

    if isinstance(json1, dict):
        mismatches = []
        for key in json1:
            if key not in json2:
                mismatches.append(f"Missing key '{path + '.' + key}' in second JSON")
            else:
                mismatches.extend(compare_json_structures(json1[key], json2[key], path + "." + key))
        for key in json2:
            if key not in json1:
                mismatches.append(f"Extra key '{path + '.' + key}' in second JSON")
        return mismatches

    elif isinstance(json1, list):
        if len(json1) != len(json2):
            return [f"List length mismatch at {path}: {len(json1)} != {len(json2)}"]
        for i, (item1, item2) in enumerate(zip(json1, json2)):
            mismatches = compare_json_structures(item1, item2, f"{path}[{i}]")
            if mismatches:
                return mismatches
    return []


import unittest

class TestJsonStructure(unittest.TestCase):
    def test_json_files(self):
        # Load JSON files
        file1 = "json_delta/en_US.json"
        file2 = "json_delta/en_US.json"
        
        json1 = load_json(file1)
        json2 = load_json(file2)

        # Compare structures
        mismatches = compare_missing_entries(json1, json2)

        # Assert no mismatches
        self.assertEqual(mismatches, [], f"JSON structure mismatches: {mismatches}")

if __name__ == "__main__":
    unittest.main()