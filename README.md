# MockCodingInterview
Resolution of a problem proposed in a Google interview. The problem can be seen here https://www.youtube.com/watch?v=3Q_oYDQ2whs. The problem it is, about 2 people who want to have a 30 minute meeting and both have calendars, each calendar with different occupied blocks, and it is intended to discover the blocks of time that both have free to get together. Each has a start and end time at which they accept meetings.

I resolve the problem, but I don't know if is right or wrong or even completed, in other words, if I cover all the cenarios.

### Sample Input:

calendar1 = [ ['9:00','10:30'] , ['12:00', '13:00'] , ['16:00','18:00'] ]

start_end1 = ['9:00', '20:00']


calendar2 = [ ['10:00','11:30'] , ['12:30', '14:30'] , ['14:30','15:00'] , ['16:00','17:00'] ]

start_end2 = ['10:00', '18:30']

block_min = 30

### Sample output : [ ['11:30','12:00'] , ['15:00', '16:00'], ['18:00','18:30'] ]
