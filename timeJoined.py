class TimeJoined:
    """Holds the time when a member joined the club
    """


    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def __init__ (self, time :str) -> None:

        #temp var assignments, update with actual values
        time = time.split()
        self.year = int(time[0])
        self.month = int(time[1])
        self.day = int(time[2])
        self.hour = int(time[3])
        self.minute = int(time[4])
        self.second = int(time[5])


    def __str__(self) -> str:
        """Return a string representation of this event.

        """
        print(self.month + "/" + self.day + "/" + self.year + " " + self.hour + ":" + self.minute + ":" + self.second)