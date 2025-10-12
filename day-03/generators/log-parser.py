# 1.  Ingest the log lines
# 2.  Filter log lines based on either level or message substring
# 3.  Extract and return only the message attribute of the logs

import sys
import json

def read_log(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)
    
log_gen = read_log("log.txt")
# print(log_gen)
# #print(next(log_gen))
# for i in range(2):
#     print(next(log_gen))

print("###################################")
def filter_logs(logs, level=None,message_str=None):
    for log in logs:
        if (
            level is not None
            and log.get("level", "").lower() != level.lower()
        ):
            continue
        if (
            message_str is not None
            and message_str.lower() not in log.get("message","").lower()
        ):
            continue
        yield log
        

fil_log=filter_logs(log_gen,'ERROR')
for i in range(20):
    print(next(fil_log))


