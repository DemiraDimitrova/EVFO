import os
import re
from datetime import datetime

def convert_to_syslog_format(log):
    """
    Converts a log entry to syslog format (RFC5424)
    """
    # Split the log into components
    date_str, _, _, message = log.split(' ', 3)
    message = message.strip()

    # Parse the date string into a datetime object
    date = datetime.strptime(date_str, '%a %b %d %H:%M:%S %Y')

    # Format the date according to RFC5424
    date_str = date.strftime('%Y-%m-%dT%H:%M:%S')

    # Construct the syslog message
    syslog_msg = f'<14>1 {date_str} localhost python - - - {message}'

    return syslog_msg

def main():
    folder_path = '/Users/cp/Desktop/logs/'
    output_file = '/Users/cp/Desktop/file.log'

    # Read all files in the folder
    logs = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.log'):
            with open(os.path.join(folder_path, filename), 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and 'script not found' not in line and 'unable to stat' not in line:
                        syslog_msg = convert_to_syslog_format(line)
                        logs.append(syslog_msg)

    # Sort the logs by date
    logs = sorted(logs)

    # Write the logs to the output file
    with open(output_file, 'w') as f:
        for log in logs:
            f.write(log + '\n')

if __name__ == '__main__':
    main()
