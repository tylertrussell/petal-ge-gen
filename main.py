#! /usr/bin/env python3

import argparse
import json
import os
import sys
import yaml

from expectations import EXPECTATIONS


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('config_yml_file_path')
    return parser.parse_args()


def get_expectations_config(config_yml_file_path):
    with open(os.path.expanduser(config_yml_file_path), 'r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError:
            print("Error reading configuration file")
            sys.exit(1)


def main():
    args = parse_args()
    expectations_config = get_expectations_config(args.config_yml_file_path)

    data = []

    for expectation_type, config in expectations_config.items():

        expectation_cls = EXPECTATIONS.get(expectation_type)
        if not expectation_cls:
            print(f"{expectation_type} doesn't have a supported class; skipping")
            continue

        columns = config.pop('columns')
        if not columns:
            print(f"{expectation_type} doesn't have columns; skipping")
            continue

        for column in columns:
            _kwargs = {'column': column, **config}
            data.append(expectation_cls.make(**_kwargs))

    print(data)
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
