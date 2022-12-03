import json
import re
from io import TextIOWrapper

import click


@click.command()
@click.option('-o', '--output_file', type=click.File('w'), help="Output file path, if different from input file")
@click.argument('input_file', type=click.File('r'))
def format_file(input_file: TextIOWrapper, output_file: TextIOWrapper):
    with input_file:
        s = input_file.read()

    s = re.sub("[\r\n\ ]+", " ", s)  # collapse to one line
    s = re.sub(",[\ ]*}", " }", s)  # remove trailing commas
    settings_json_dict = json.loads(s)

    if output_file is None:
        output_file = open(input_file.name, 'w')
    with output_file:
        output_file.write(json.dumps(
            settings_json_dict, indent=4, sort_keys=True))


if __name__ == '__main__':
    format_file()
