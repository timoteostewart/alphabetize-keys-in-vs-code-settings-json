import json
import re
import sys


def main(json_filename):
    settings_json_dict = None
    with open(json_filename, mode="r", encoding="utf-8") as fin:
        s = fin.read()
        s = re.sub("[\r\n\ ]+", " ", s)  # collapse to one line
        s = re.sub(",[\ ]*}", " }", s)  # remove trailing commas
        settings_json_dict = json.loads(s)
    with open(json_filename, mode="w", encoding="utf-8") as fout:
        fout.write(json.dumps(settings_json_dict, sort_keys=True, indent=4))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Sorts json file alphabetically by 1st level of keys.")
        print("Usage: python main.py JSON_FILE")
        print("Example: python main.py settings.json")
        exit(0)
    exit(main(sys.argv[1]))
