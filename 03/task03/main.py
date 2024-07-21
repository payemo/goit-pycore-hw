import argparse
from SimpleLogParser import SimpleLogParser

# Define log format as a list of tuples with each header and its regex pattern.
log_format = [
    ("Date",    r"\d{4}-\d{2}-\d{2}"),
    ("Time",    "[0-2][0-9]:[0-5][0-9]:[0-5][0-9]"),
    ("Level",   "INFO|WARNING|DEBUG|ERROR"),
    ("Content", ".*")
]

def main():
    arg_parser = argparse.ArgumentParser(description="Utility for parsing log file.")
    arg_parser.add_argument('-f', '--filter', type=str, help="Filters logs by specified log level.")
    arg_parser.add_argument('-s', '--statistics', type=bool, help="Display statistics by each log level.", default=True)

    args = arg_parser.parse_args()

    try:
        log_parser = SimpleLogParser(log_format)
        log_parser.parse(log_file)

        # Show statistics if requested.
        if args.statistics:
            log_parser.display_log_level_statistics()

        # Filter logs if a filter is provided.
        if args.filter:
            print(f"\nDetails for log level '{args.filter.upper()}':")
            for log in log_parser.filter_by_log_level_generator(args.filter):
                print(log)
            
    except Exception as e:
        print(f"Unexpected error: {e}.")

if __name__ == '__main__':
    log_file = 'simple_log01.txt'
    main()
