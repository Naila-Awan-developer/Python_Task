class WeekDayError(Exception):
    pass
class Weeker:

    def __init__(self, day):
        self.__days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        if day not in self.__days:
            raise WeekDayError(f"Invalid weekday: {day}")
        self.__day = day

    def __str__(self):
        return self.__day
    def add_days(self, n):
        index = self.__days.index(self.__day)
        self.__day = self.__days[(index + n) % 7]
    def subtract_days(self, n):
        index = self.__days.index(self.__day)
        self.__day = self.__days[(index - n) % 7]

try:
    weeker = Weeker("Mon")
    print(weeker)
    weeker.add_days(15)
    print(weeker)
    weeker.subtract_days(23)
    print(weeker)
    weeker = Weeker("Monday")
except WeekDayError:
    print("Sorry, I can't serve your request.")
    