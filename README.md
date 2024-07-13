---

# Log Parser

## Overview

This project is a Python-based log parser designed to read and analyze log files. The parser extracts and processes log entries, providing insights into the events recorded in the logs.

## Files

- `example_log.txt`: A sample log file containing log entries.
- `log_parser.py`: The main script that parses the log file and processes the log entries.
- `log_row.py`: Contains the structure and processing logic for individual log entries.

## Repository

[GitHub Repository Link](https://github.com/b3dniy/log_parser)

## Usage

### Prerequisites

- Python 3.x

### Setup

1. Clone the repository:

```bash
git clone https://github.com/b3dniy/log_parser.git
cd log_parser
```

2. Install any required dependencies (if applicable):

```bash
pip install -r requirements.txt
```

### Running the Log Parser

1. Ensure `example_log.txt` is in the same directory as `log_parser.py`.

2. Run the log parser script:

```bash
python log_parser.py example_log.txt
```

This will parse the log file and output the processed log entries.

## Details

### example_log.txt

This file contains sample log entries that will be parsed by the script. Each log entry follows a specific format with a timestamp, log level, and message.

Example log entries:

```plaintext
03/22 08:53:52 TRACE  :.......rsvp_parse_objects: STYLE is WF
03/22 08:53:52 INFO   :.......rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0
03/22 08:53:52 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists
03/22 08:53:52 INFO   :.......rsvp_flow_stateMachine: state RESVED, event RESV
```

### log_parser.py

This is the main script responsible for reading the log file, parsing each entry, and processing the logs. It utilizes the `log_row.py` module to handle individual log entries.

### log_row.py

This script defines the structure and processing logic for individual log entries. It includes methods to parse the log format and extract relevant information from each log entry.

## Example Output

The script processes the log entries and prints the parsed information. For example:

```plaintext
Parsed log entries:
Timestamp: 03/22 08:53:52, Level: TRACE, Message: rsvp_parse_objects: STYLE is WF
Timestamp: 03/22 08:53:52, Level: INFO, Message: rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0
...
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---
