class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_elapsed_time(self):
        s = self._hours * 3600 + self._minutes * 60 + self._seconds
        return s

    def set_elapsed_time(self, seconds):
        if seconds > 86400:
            seconds %= 86400
            self._hours = seconds // 3600
            self._minutes = seconds % 3600 // 60
            self._seconds = seconds - self._hours * 3600 - self._minutes * 60
        else:
            self._hours = seconds // 3600
            self._minutes = seconds % 3600 // 60
            self._seconds = seconds - self._hours * 3600 - self._minutes * 60

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        self._hours = hours

    def get_minutes(self):
        return self._minutes

    def set_minutes(self, minutes):
        self._minutes = minutes

    def get_seconds(self):
        return self._seconds

    def set_seconds(self, seconds):
        self._seconds = seconds

    def __str__(self):
        return 'Time: ' + str(self._hours) + ":" + str(self._minutes) + ":" + str(self._seconds)

    elapsed_time = property(get_elapsed_time, set_elapsed_time)
    hours = property(get_hours, set_hours)
    minutes = property(get_minutes, set_minutes)
    seconds = property(get_seconds, set_seconds)