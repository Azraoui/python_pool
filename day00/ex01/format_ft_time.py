# import time

# # get the current time in seconds since epoch
# epoch_time = time.time()

# # format the epoch time
# formatted_time = "{:,.4f}".format(epoch_time)

# # format the date
# date = time.strftime("%b %d %Y", time.localtime(epoch_time))

# # print the formatted output
# print("Seconds since January 1, 1970: {} or {:.2e} in scientific notation\n{}".format(formatted_time, epoch_time, date))

import datetime

# get the current date and time
now = datetime.datetime.now()

# format the date and time
formatted_date = now.strftime("%b %d %Y")
formatted_time = now.strftime("%I:%M:%S %p")

# print the formatted output
print("Today's date: {}".format(formatted_date))
print("Current time: {}".format(formatted_time))
