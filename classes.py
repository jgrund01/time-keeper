class Shift:
    FILE_PATH = "./"
    FILE_NAME = "time_keeper_log.txt"
    FULL_PATH = FILE_PATH + FILE_NAME

    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, date, start_time, lunch_start, lunch_end, end_time):
        self.date = date
        self.start_time = start_time
        self.lunch_start = lunch_start
        self.lunch_end = lunch_end
        self.end_time = end_time

    def save(self):
        f = open(self.FULL_PATH, 'a+')

        f.write("DATE: " + self.date.strftime(self.DATE_FORMAT) +
                " START_TIME: " + self.start_time +
                " LUNCH_START: " + self.lunch_start)

        f.close()
