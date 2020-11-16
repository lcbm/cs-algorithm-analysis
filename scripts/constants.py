""" Constants uses across the scripts. """

EOF = ""
SEPARATOR = ","

INDEX_COL_FIRST = "algorithm"
INDEX_COL_SECOND = "entries"


INPUT_FILE_SEPARATOR = "\t"
INPUT_FILE_EXTENSION = ".txt"


DATA_PATH = "data"
OUTPUT_FILE = f"{DATA_PATH}/execution_times.csv"


FIGURES_PATH = "figures"
FIGURES_EXTENSION = ".png"


GNOME_SORT = "gnome_sort"
COCKTAIL_SORT = "cocktail_sort"
SELECTION_SORT = "selection_sort"
MERGE_SORT = "merge_sort"

SUPPORTED_ALGORITMS = [GNOME_SORT, COCKTAIL_SORT, SELECTION_SORT, MERGE_SORT]


AVERAGE = "average"
BEST = "best"
WORST = "worst"
CASES = [AVERAGE, BEST, WORST]
