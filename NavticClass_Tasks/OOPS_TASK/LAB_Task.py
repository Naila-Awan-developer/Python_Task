#Timer Task
def format_time(hours, minutes, seconds): #Format time as 'hh:mm:ss' with leading zeros.
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class Timer:#Class to count seconds.


    def __init__(self, hours=0, minutes=0, seconds=0):  #Initialize Timer object.
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self): #Return string representation of Timer object.
        return format_time(self.__hours, self.__minutes, self.__seconds)

    def next_second(self): #Increment time by 1 second.
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def previous_second(self): #Decrement time by 1 second.

        if self.__seconds == 0:
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23
            self.__seconds = 59
        else:
            self.__seconds -= 1


timer = Timer(12, 30, 45)
print(timer)  # Output: 12:30:45
timer.next_second()
print(timer)  # Output: 12:30:46
timer.previous_second()
print(timer)  # Output: 12:30:45