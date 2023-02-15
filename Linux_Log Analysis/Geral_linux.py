import os
import re

def parse_log(logfile):
    suspicious_activities = []
    with open(logfile, 'r') as f:
        logs = f.readlines()
        for i, log in enumerate(logs):
            if 'Failed password' in log:
                suspicious_activities.append(('Failed password attempt', i+1, logfile))
            elif 'Invalid user' in log:
                suspicious_activities.append(('Invalid user attempt', i+1, logfile))
            elif 'Accepted password' in log and 'for illegal user' in log:
                suspicious_activities.append(('Accepted password for illegal user', i+1, logfile))
            elif 'reverse mapping' in log and 'checking getaddrinfo' in log:
                suspicious_activities.append(('Reverse mapping checking getaddrinfo for server', i+1, logfile))
    return suspicious_activities
def main():
    logs_path = '/var/log/'
    log_files = [f for f in os.listdir(logs_path) if f.endswith('.log')]
    suspicious_activities = []
    for log_file in log_files:
        activities = parse_log(logs_path + log_file)
        suspicious_activities += activities
    if suspicious_activities:
        print('Found suspicious activities:')
        for activity, line_num, file_name in set(suspicious_activities):
            print('- ' + activity + ' in line ' + str(line_num) + ' of ' + file_name)
    else:
        print('No suspicious activities found.')

if __name__ == '__main__':
    main()
