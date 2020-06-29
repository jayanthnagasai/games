import datetime
import os
import time
import random
import webbrowser

if not os.path.isfile("youtube_alarm_videos"):
    print('Creating "youtube_alarm_videos"...')
    with open("youtube_alarm_videos.txt" , "w") as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=wSPjbiy0Zv0")

def check_alarm_input(alarm_time):
    if len(alarm_time) == 1:
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
            alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
            alarm_time[1] < 60 and alarm_time[1] >= 0 and \
            alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False

print("Set a time for alarm [HH:MM or HH:MM:SS]")
while True:
    alarm_input = input("Enter here:   ")
    try:
        alarm_time = [int(n) for n in alarm_input.split(":")]
        if check_alarm_input(alarm_time):
            break
        else:
            raise ValueError
    except ValueError:
        print("Error! Enter time in HH:MM or HH:MM:SS")

seconds_hms = [3600, 60, 1]
alarm_seconds = sum( [a*b for a,b in zip(seconds_hms[: len(alarm_time)], alarm_time)])

now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second, now.microsecond])])

time_diff_seconds =  alarm_seconds - current_time_seconds

if time_diff_seconds < 0:
    time_diff_seconds += 86400

print("Alarm set to off in %s" % datetime.timedelta(seconds=time_diff_seconds))
print("Ring!")

with open("youtube_alarm_videos.txt", "r") as alarm_file:
    videos = alarm_file.readlines()

webbrowser.open(random.choice(videos))


