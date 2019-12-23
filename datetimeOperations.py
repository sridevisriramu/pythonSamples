from datetime import datetime
now = datetime.now()

print '%02d-%02d-%04d' % (now.month, now.day, now.year)

print now.hour
print now.minute
print now.second

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

print '%02d/%02d/%04d %02d:%02d:%02d  ' % (now.month, now.day, now.year, now.hour, now.minute, now.second) 