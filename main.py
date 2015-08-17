import time
import datetime
from classes import Shift

DATE_FORMAT = "YYYY-MM-DD"
TIME_FORMAT = "%H:%M"

# check if it is an entry for today
today_entry_answer = raw_input("Is this a work entry for today?")

current_date = 0;

while current_date == 0:
    # check the input the user supplied
    if today_entry_answer == 'y' or today_entry_answer == "yes":
        current_date = datetime.datetime.now().date()

    elif today_entry_answer == 'n' or today_entry_answer == "no":
        current_date = raw_input("What is today's date? " + DATE_FORMAT + ": ")

    else:
        print "You entered something other than yes/no.  Please enter yes(y)/no(n)"

print current_date

work_start = raw_input("When did you get to work? FORMAT: HH:MM Military Time \n")
formatted_work_start = time.strptime(work_start, TIME_FORMAT)

lunch_start = raw_input("When did you take a lunch? FORMAT: HH:MM Military Time\n")
formatted_lunch_start = time.strptime(lunch_start, TIME_FORMAT)

lunch_end = raw_input("When did you finish feeding your fat ass? FORMAT: HH:MM Military Time\n")
formatted_lunch_end = time.strptime(lunch_end, TIME_FORMAT)

work_end = raw_input("When did you leave that god forsaken place you call work? FORMAT: HH:MM Military Time\n")
formatted_work_end = time.strptime(work_end, TIME_FORMAT)


# create a new shift object to store that shift data
new_shift = Shift(date=current_date, start_time=work_start, lunch_start=lunch_start, lunch_end=lunch_end,
                  end_time=work_end)


# save the shift once the user is satisified with the input
new_shift.save()
