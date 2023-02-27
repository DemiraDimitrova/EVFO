import os
import re
import datetime

# Define the log files directory
log_dir = "/Users/cp/Desktop/logs/"

# Define the regex pattern to extract the date and time from the log line
date_pattern = r"^\w{3} \d{1,2} \d{2}:\d{2}:\d{2}"

# Define a function to convert a log line to the syslog-RFC5424 format
def convert_to_syslog(line):
    # Extract the date and time from the log line
    date_time_str = re.search(date_pattern, line).group()
    date_time_obj = datetime.datetime.strptime(date_time_str, "%b %d %H:%M:%S")
    # Build the syslog message
    syslog_msg = f"<34>1 {date_time_obj.isoformat()}+00:00 {os.uname().nodename} app - - {line}"
    return syslog_msg

# Define a list to store the syslog messages
syslog_msgs = []

# Loop through each file in the log files directory
for filename in os.listdir(log_dir):
    if filename.endswith(".log"):
        # Open the file and read its lines
        with open(os.path.join(log_dir, filename)) as file:
            lines = file.readlines()
        # Loop through each line in the file
        for line in lines:
            # If the line contains the date and time, convert it to the syslog format and add it to the syslog messages list
            date_time = re.search(date_pattern, line)
            if date_time:
                syslog_msgs.append((datetime.datetime.strptime(date_time.group(), "%b %d %H:%M:%S"), convert_to_syslog(line)))

# Sort the syslog messages by date and time
syslog_msgs.sort()

# Define the output file path
output_file = "/Users/cp/Desktop/file.log"

# Open the output file and write the sorted syslog messages to it
with open(output_file, "w") as file:
    for msg in syslog_msgs:
        file.write(msg[1])

# Print a message to indicate the program has completed
print(f"Syslog messages saved to {output_file}")
