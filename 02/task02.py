from pathlib import Path

def get_cats_info(path:str) -> list[dict]:
    """Parse file with information about cats. File contains ONLY unique cat's identifiers.
    No duplication handling exists.
    
    Parameters:
        path: Path to the file with cats information.

    Returns:
        List of dictionaries containing information about each cat.

    Raises:
        FileNotFoundError:
            If file cannot be found by input path.
        PermissionError:
            If there are insufficient permissions to read the file.
        ValueError:
            If a line cannot be parsed correctly.
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File cannot be found: {file_path.name}")
    
    cats_info = []

    with file_path.open('r', encoding='utf-8') as file:
        try:
            for line in file:
                guid, name, age = line.strip().split(',')
                cats_info.append({"id": guid, "name": name, "age": int(age)})
        except Exception:
            raise ValueError(f"Malformed line: {line}")
            
    return cats_info

def main():
    path = (Path(__file__).parent / 'content' / 'cats_info.txt').as_posix()

    try:
        cats_info = get_cats_info(path)
        print(cats_info)
    except (FileNotFoundError, PermissionError, ValueError) as e:
        print(f"Error occurred: {e}")

if __name__ == '__main__':
    main()