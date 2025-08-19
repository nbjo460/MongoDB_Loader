class soldier:
    def __init__(self, __id, _first_name, _last_number, _phone_number, _rank):
        self._id = __id
        self.first_name = _first_name
        self.last_name = _last_number
        self.phone_number = _phone_number
        self.rank = _rank

    def __str__(self):
        return (f"id:{self._id}\n"
                f"first name: {self.first_name}\n"
                f"last name: {self.last_name}\n"
                f"phone number: {self.phone_number}\n"
                f"rank: {self.rank}")