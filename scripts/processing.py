""" Python script for IO (Input-Output) stream handling for this activity. """

import os

import constants
import pandas as pd


def read_input_from_file(file: str) -> list:
    """ Function to retrieve data from a file. """
    input = []
    filepath = f"{constants.DATA_PATH}/{file}" + constants.INPUT_FILE_EXTENSION
    with open(filepath, "r") as reader:
        next(reader)
        line = reader.readline()
        while line != constants.EOF:
            parsed_line = line.replace(
                constants.INPUT_FILE_SEPARATOR, constants.SEPARATOR
            ).split(constants.SEPARATOR)
            elements = [int(element) for element in parsed_line]
            input.extend(elements)
            line = reader.readline()

    return input


def get_sorted_files() -> list:
    """ Function to retrieve data files in sorted fashion. """
    files = [
        file.replace(constants.INPUT_FILE_EXTENSION, "")
        for file in os.listdir(constants.DATA_PATH)
        if file.endswith(constants.INPUT_FILE_EXTENSION)
    ]
    return sorted(files, key=int)


def save_to_csv(file_name: str, data: dict) -> None:
    """ Function to save nested dicts to a CSV file. """
    df = pd.DataFrame.from_dict(
        {
            (entries, time): data[entries][time]
            for entries in data.keys()
            for time in data[entries].keys()
        },
        orient="index",
    )
    df.index.set_names(
        [constants.INDEX_COL_FIRST, constants.INDEX_COL_SECOND], inplace=True
    )
    df.to_csv(file_name)
