import argparse
from pathlib import Path
from colorama import Fore

def walk_dir(path:Path, depth:int = 0):
    """
    Generator that yields directory contents with their depth level.

    Args:
        path (Path): The directory path to walk through.
        depth (int): The current depth level, defaults to 0.

    Yields:
        tuple: A tuple containing the item (directory/file) and its depth level.
    """
    for item in path.iterdir():
        yield item, depth
        if item.is_dir():
            yield from walk_dir(item, depth + 1)

def print_dir_info(path:str) -> None:
    """
    Prints the directory structure starting from the given path.

    Args:
        path (str): The root directory path to start printing from.

    Raises:
        FileNotFoundError:
            If the specified path does not exist.
        PermissionError: 
            If the permissions do not allow reading the directory.
    """
    try:
        dir_path = Path(path).resolve(strict=True)

        # Print root directory.
        print(f"{Fore.BLUE} {dir_path.stem}/")

        for item, depth in walk_dir(dir_path, 1):
            indent = '  ' * depth
            if item.is_dir():
                print(f"{Fore.BLUE} {indent}{item.name}/")
            else:
                print(f"{Fore.GREEN} {indent}{item.name}")
    except FileNotFoundError as fnf_error:
        print(f"Error: Directory not found - {fnf_error}")
    except PermissionError as perm_error:
        print(f"Error: Permission denied - {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Utility for printing directory structure.")
    parser.add_argument('-p', '--path', type=str, help='Path to the directory which structure will be printed.')

    args = parser.parse_args()

    if args.path:
        print_dir_info(args.path)
    else:
        print("Invalid input argument.")
        

if __name__ == '__main__':
    main()