""" Python script to compare execution time of sorting algorithms. """

import collections
import sys
import time

import algorithms
import constants
import mock
import pandas as pd
import plot
import processing

# https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
sys.setrecursionlimit(10 ** 6)


def __timed_run(algorithm, data, case, entries) -> str:
    print(f"\n>>>>>> {algorithm}: sorting {case} {entries} entries...")
    start = time.process_time()
    algorithms.run(algorithm, data)
    execution_time = str(round((time.process_time() - start), 4))
    print(
        f"\n>>>>>> {algorithm}: sorted {case} {entries} entries in {execution_time} seconds."
    )

    return execution_time


if __name__ == "__main__":
    execution_times = collections.defaultdict(dict)

    for file in processing.get_sorted_files():
        print(f"\n\n>> Processing file with {file} entries...")
        data = processing.read_input_from_file(file)

        print("\n>>>> Generating best and worst cases based on file data...")
        best, worst, merge_worst = mock.best_and_worst_cases(int(file))

        for algorithm in constants.SUPPORTED_ALGORITMS:
            execution_times[algorithm][file] = {}

            avg_case_time = __timed_run(algorithm, data[:], constants.AVERAGE, file)
            execution_times[algorithm][file].update({constants.AVERAGE: avg_case_time})

            best_case_time = __timed_run(algorithm, best[:], constants.BEST, file)
            execution_times[algorithm][file].update({constants.BEST: best_case_time})

            worst_case = merge_worst if algorithm is constants.MERGE_SORT else worst
            worst_case_time = __timed_run(
                algorithm, worst_case[:], constants.WORST, file
            )
            execution_times[algorithm][file].update({constants.WORST: worst_case_time})

    processing.save_to_csv(constants.OUTPUT_FILE, execution_times)

    dataframe = pd.read_csv(constants.OUTPUT_FILE)
    plot.algorithm_execution_times(dataframe, constants.SUPPORTED_ALGORITMS)
    plot.cases_execution_times(dataframe, constants.CASES)
