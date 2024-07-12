from pathlib import Path

def total_salary(path: str) -> tuple[int, float]:
    """Calculate the total and average salary of developers from a file.

    This function reads a file where each line contains a developer's last name and salary,
    separated by a comma, with no spaces. It calculates and returns the total and average
    salaries of all developers listed in the file.

    Parameters:
        path (str): The path to the text file containing salary information.

    Returns:
        tuple[int, float]: A tuple containing:
            - Total salary of all developers (int).
            - Average salary of all developers (float).

    Raises:
        FileNotFoundError
            If the specified file does not exist.
        PermissionError 
            If the file cannot be read due to permission issues.
        ValueError 
            If there is an issue with file content (e.g., malformed lines or no valid salary data).
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {file_path.name}.")

    salaries = []

    with file_path.open(mode='r', encoding='utf-8') as file:
        for line in file:
            try:
                # Retrieve salary.
                salary = int(line.strip().split(',')[1])
                salaries.append(salary)
            except (ValueError, IndexError):
                raise ValueError(f"Malformed line: {line.strip()}")
            
    if not salaries:
        raise ValueError("No valid salary data found.")

    total = sum(salaries)
    return total, total / len(salaries)
    
def main():
    # Build the path and return it as string in POSIX format.
    path = (Path(__file__).parent / 'content' / 'salaries.txt').as_posix()

    try:
        total, avg = total_salary(path)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avg:.2f}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == '__main__':
    main()