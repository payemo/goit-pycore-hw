import re
from typing import Pattern, Counter, Generator, List, Tuple

class SimpleLogParser:
    """
    SimpleLogParser class for parsing log files based on a specified format.
    """

    def __init__(self, log_format: List[Tuple[str, str]], indir='./') -> None:
        """
        Initialize the SimpleLogParser with a log format and an optional directory.
        
        Args:
            log_format (List[Tuple[str, str]]): List of headers and their corresponding regex patterns.
            indir (str): Directory where the log files are located.
        """
        self.path = indir
        self.log_format = log_format
        self.log_messages = []
        self.linecount = 0

    def parse(self, logname: str) -> None:
        """
        Parse the log file and store the log splitted messages: [<Date>, <Time>, <Level>, <Content>].
        
        Args:
            logname (str): Name of the log file to parse.
        """
        headers, regex = self.generate_logformat_regex(self.log_format)

        for line in self.load_data(logname):
            match = regex.search(line.strip())
            try:
                if match:
                    message = [match.group(header) for header in headers]
                    self.log_messages.append(message)
                    self.linecount += 1
                else:
                    print(f"[Warning] Line does not match the format: {line.strip()}")
            except Exception as e:
                print(f"[Error] Failed to parse line: {line.strip()}. Error: {e}")
    
    def count_by_level(self) -> Counter:
        """
        Count the number of log messages by log level.
        
        Returns:
            Counter: A counter object with the count of messages per log level.
        """
        return Counter([msg[2] for msg in self.log_messages])

    def generate_logformat_regex(self, logformat: List[Tuple[str, str]]) -> Tuple[List[str], Pattern]:
        """
        Generate a regex pattern based on the log format.
        
        Args:
            log_format (List[Tuple[str, str]]): List of headers and their corresponding regex patterns.
        
        Returns:
            Tuple[List[str], Pattern]: List of headers and the compiled regex pattern.

        Example:
            Pattern: (?P<Date>\d{4}-\d{2}-\d{2})\s+(?P<Time>[0-2][0-9]:[0-5][0-9]:[0-5][0-9])\s+(?P<Level>INFO|WARNING|DEBUG|ERROR)\s+(?P<Content>.*)
            Text: 2024-01-22 08:30:01 INFO User logged in successfully
        """
        headers = [pair[0] for pair in logformat]
        regex = r"\s+".join(f"(?P<{header}>{pattern})" for header, pattern in logformat)

        return headers, re.compile(f"^{regex}$")
    
    def load_data(self, path: str) -> Generator[str, None, None]:
        """
        Load data from the log file.
        
        Args:
            path (str): Path to the log file.
        
        Yields:
            Generator[str, None, None]: Generator yielding lines from the log file.
        """
        try:
            with open(path, 'r', encoding='utf-8') as log_file:
                for line in log_file:
                    yield line
        except FileNotFoundError:
            print(f"[Error] File not found: {path}")
        except Exception as e:
            print(f"[Error] Error reading file: {path}. Error: {e}")

    def display_log_level_statistics(self) -> None:
        """
        Display the count of log messages by log level in a formatted table.

        Sample output:
            | Log level | Count |
            | --------- | ----- |
            | INFO      | 4     |
            | DEBUG     | 3     |
            | ERROR     | 2     |
            | WARNING   | 1     |
        """
        levels = self.count_by_level()

        print(f"{'Log level':<15}| {'Count':<6}")
        print(f"{'-' * 15}|{'-' * 6}")
        for lvl, cnt in levels.items():
            print(f"{lvl:<15}| {cnt:<6}")

    def filter_by_log_level(self, log_lvl: str) -> List[str]:
        """
        Filter log messages by a specified log level.
        
        Args:
            log_lvl (str): Log level to filter by.
        
        Returns:
            List[str]: List of log messages that match the specified log level.
        """
        filtered_logs = filter(lambda log_msg: log_msg[2].lower() == log_lvl.lower(), self.log_messages)
        return [f"{date} {time} - {content}" for date, time, _, content in filtered_logs]
    
    def filter_by_log_level_generator(self, log_lvl: str) -> Generator[str, None, None]:
        """
        Filter log messages by a specified log level using a generator.
        
        Args:
            log_lvl (str): Log level to filter by.
        
        Yields:
            Generator[str, None, None]: Generator yielding log messages that match the specified log level.
        """
        for date, time, _, content in filter(lambda log_msg: log_msg[2].lower() == log_lvl.lower(), self.log_messages):
            yield f"{date} {time} - {content}"

    