# Sample Input:

calendar1 = [ ['9:00','10:30'] , ['12:00', '13:00'] , ['16:00','18:00'] ]
start_end1 = ['9:00', '20:00']

calendar2 = [ ['10:00','11:30'] , ['12:30', '14:30'] , ['14:30','15:00'] , ['16:00','17:00'] ]
start_end2 = ['10:00', '18:30']

block_min = 30

# Sample output : [ ['11:30','12:00'] , ['15:00', '16:00'], ['18:00','18:30'] ]

from datetime import datetime, timedelta

start, end = max(datetime.strptime(start_end1[0], '%H:%M'),datetime.strptime(start_end2[0], '%H:%M')), min(datetime.strptime(start_end1[1], '%H:%M'),datetime.strptime(start_end2[1], '%H:%M'))
print("\n","Max first hour available between the two calendars: ",start.time(),"\n","Min last  hour available between the two calendars: ",end.time(),"\n")

# silence times for calendar 1
silence_times1 = [datetime.strptime(y[0], '%H:%M')  - datetime.strptime(x[1], '%H:%M') for x,y in zip(calendar1,calendar1[1:])]
result1 = [ [datetime.strptime(x[1], '%H:%M'), datetime.strptime(x[1], '%H:%M') + silence_times1[index]] for index, x in enumerate(calendar1[:-1]) if silence_times1[index] > timedelta(seconds=0) ]

# first hour busy
begin = datetime.strptime(calendar1[0][0], '%H:%M')

# last hour busy
finish = datetime.strptime(calendar1[-1][1], '%H:%M')

# silence time between the availability start value until the beginning of the first busy hour.
if begin > start and begin - start >= timedelta(minutes=block_min):
    result1[:-1] = [start, begin]

# append silence time enter the value from the end of the calendar until the last hour that is available.
if end > finish and end - finish >= timedelta(minutes=block_min):
    result1.append([finish, end])

print("Silence times from Calendar 1: ",[[str(x[0].time()), str(x[1].time())] for x in result1])

# silence times for calendar 2
silence_times2 = [datetime.strptime(y[0], '%H:%M')  - datetime.strptime(x[1], '%H:%M') for x,y in zip(calendar2,calendar2[1:])]
result2 = [ [datetime.strptime(x[1], '%H:%M'), datetime.strptime(x[1], '%H:%M') + silence_times2[index]] for index, x in enumerate(calendar2[:-1]) if silence_times2[index] > timedelta(seconds=0) ]

# first hour busy
begin = datetime.strptime(calendar2[0][0], '%H:%M')

# last hour busy
finish = datetime.strptime(calendar2[-1][1], '%H:%M')

# silence time between the availability start value until the beginning of the first busy hour.
if begin > start and begin - start >= timedelta(minutes=block_min):
    result2[:-1] = [start, begin]

# append silence time enter the value from the end of the calendar until the last hour that is available.
if end > finish and end - finish >= timedelta(minutes=block_min):
    result2.append([finish, end])

print("Silence times from Calendar 2: ",[[str(x[0].time()), str(x[1].time())] for x in result2])

final_result = [[str(max([x[0],y[0]]).time()), str(min(x[1],y[1]).time())] for x,y in zip(result1,result2)]
print("Silence times between the two calendars : ", final_result)

