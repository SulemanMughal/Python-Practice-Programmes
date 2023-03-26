# Python time method time() returns current time as  floating point number expressed in seconds since the epoch, in UTC
# Pythom time method asctime() converts a struct_time representing a time as returned by gmtime() or localtime() to a 24-character string of the following form: 'Fr Sep 10 11:27:05 2021'.
import time; 
print(time.time())
print(time.asctime( time.localtime(time.time())))