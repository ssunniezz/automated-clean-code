# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse
from typing import Dict, List


def main():
    """Run all the features.

    Returns:
        None

    """
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    args = parser.parse_args()

    # fill up histogram
    with open(args.fname, "r") as f:
        counter = fill_up_histogram_from_list(list(f))

    # find max key
    max_key, max_counter, min_key, min_counter = find_max_key(counter)

    print(f"Min Key = {min_key} with count = {min_counter}")
    print(f"Max Key = {max_key} with count = {max_counter}")


def fill_up_histogram_from_list(lst: List[str]) -> Dict[str, int]:
    """Fill up the histogram from input lst.

    Args:
        lst: list of string

    Returns:
        dictionary of string, numbers

    """
    counter = {}

    for element in lst:
        element = element.strip()
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1

    return counter


def find_max_key(counter: Dict[str, int]) -> (str, int, str, int):
    """Find max key from a given dict.

    Args:
        counter: dictionary of string, numbers

    Returns:
        tuple of string, numbers, string, numbers

    """
    max_key = None
    max_counter = 0
    min_key = None
    min_counter = 0

    for k, v in counter.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v

    return max_key, max_counter, min_key, min_counter


if __name__ == "__main__":
    main()
