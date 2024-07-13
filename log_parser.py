import re
from log_row import LogRow

def parse_log_line(log_line):
    # Регулярные выражения для извлечения данных из строки лога
    time_pattern = r'^(\d{2}/\d{2} \d{2}:\d{2}:\d{2})'
    type_pattern = r'\b(TRACE|INFO|EVENT)\b'
    message_pattern = r'(?<=:\s).*$'

    # Поиск данных в строке лога
    time_match = re.search(time_pattern, log_line)
    type_match = re.search(type_pattern, log_line)
    message_match = re.search(message_pattern, log_line)

    if time_match and type_match and message_match:
        event_time = time_match.group(1)
        event_type = type_match.group()
        event_message = message_match.group()
        return LogRow(event_time, event_type, event_message)
    else:
        return None

def parse_log_file(file_path):
    log_rows = []
    with open(file_path, 'r') as file:
        for line in file:
            row = parse_log_line(line)
            if row:
                log_rows.append(row)
    return log_rows

# Пример использования
if __name__ == "__main__":
    log_file_path = "C:/Users/Dmitry.Kozlov/Desktop/projects/log_parsing/example_log.txt" # Путь к файлу с логом
    logs = parse_log_file(log_file_path)
    for log in logs:
        print(f"Time: {log.event_time}, Type: {log.event_type}, Message: {log.event_message}")
