import datetime
from collections import defaultdict

# def calculate_mean_from_log_files(lines):
#     duration = defaultdict(int)
#     for line in lines:
#         timestamp, action, id = line.split()
#         if action == "Started":
#             duration[id] = timestamp_to_seconds(timestamp)
#         elif action == "Finished":
#             duration[id] = timestamp_to_seconds(timestamp) - duration[id]

#     return sum(duration.values()) / len(duration)

def calculate_mean_from_log_files(lines):
    duration = defaultdict(list)
    count = 0
    for line in lines:
        timestamp, _, id = line.split()
        if id in duration:
            count += timestamp_to_seconds(timestamp) - duration[id][0] # because it's a list
        else:
            duration[id] = [timestamp_to_seconds(timestamp)]

    return count / len(duration)


def timestamp_to_seconds(timestamp):
    return datetime.datetime.fromisoformat(timestamp).timestamp()

input = [
    "2020-07-01T14:10:10.100 Started #4257",
    "2020-07-01T14:10:10.250 Started #4258",
    "2020-07-01T14:10:10.300 Finished #4258",
    "2020-07-01T14:10:10.320 Finished #4257"
]

mean_duration = calculate_mean_from_log_files(input)
print(mean_duration)



