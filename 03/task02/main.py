import argparse
import os
import re
from typing import Callable, Generator

input_dir = "revenues/"

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Parse input text by retrieving revenue data as floating-point numbers.

    Args:
        text (str): Input text containing revenue data.

    Yields:
        float: Parsed revenue numbers.
    """
    for match in re.finditer(r"(?<![\w.])[+-]?(\d+(\.\d*)?|\.\d+)(?![\w.])", text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculates total profit based on revenue data parsed from the input text.

    Args:
        text (str): Input text containing revenue data.
        func (Callable[[str], Generator[float, None, None]]): Generator function to parse revenue data.

    Returns:
        float: Total calculated profit.
    """
    total_profit = sum(func(text))
    return total_profit

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Utility for calculating the total income based on a data from file.")    
    parser.add_argument('-f', '--file', type=str, help="Name of the input file with data about revenue.", required=True)

    args = parser.parse_args()

    full_file_path = os.path.join(input_dir, args.file)

    if os.path.isfile(full_file_path):
        with open(full_file_path, 'r', encoding='utf-8') as f:
            # Load full text and parse income data.
            text = f.read()
            total_income = sum_profit(text, generator_numbers)
            print(f"Total income: {total_income}")
    else:
        print(f"Error: The file {args.file} does not exist in the directory '{input_dir}'.")