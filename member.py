from timeJoined import TimeJoined

class Member:
    """A member of your club


    """

    time : TimeJoined
    first_name: str
    last_name: str
    student_email: str
    student_number: int
    additional_note: str


    def __init__ (self, time: TimeJoined, first_name: str, last_name: str, student_email: str, student_number: int, additional_note: str) -> None:
        self.time = time
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.student_email = student_email
        self.additional_note = additional_note
        if str(additional_note) == "nan" or additional_note == "-" or additional_note == " ":
            self.additional_note = None

    def __str__(self) -> str:
        """Return a string representation of this event.

        """
        return_string = self.first_name + " " + self.last_name

        return return_string