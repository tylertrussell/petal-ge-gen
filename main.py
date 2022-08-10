#! /usr/bin/env python3

import argparse
import json
import os
import sys
import yaml

import expectations

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

    for expectation_type, config_list in expectations_config.items():

        if not isinstance(config_list, list):
            config_list = [config_list]

        for config in config_list:

            columns = config.pop('columns')
            if not columns:
                print(f"{expectation_type} doesn't have columns; skipping")
                continue

            for column in columns:
                _kwargs = {'column': column, **config}
                try:
                    expectation = expectations.make(expectation_type, **_kwargs)
                except AssertionError:
                    print(f"{expectation_type} failed; is it missing from the EXPECTATIONS map?")
                    break

                data.append(expectation)

    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
