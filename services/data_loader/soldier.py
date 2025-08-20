class Soldier:
    # def __init__(self, __id, _first_name, _last_number, _phone_number, _rank):
    def __init__(self, _first_name, _last_number, _phone_number, _rank):

        # self._id = __id
        self.first_name = _first_name
        self.last_name = _last_number
        self.phone_number = _phone_number
        self.rank = _rank

    def to_dict(self):
        # return {"_id":self._id, "first_name":self.first_name,
        return {"first_name":self.first_name,
                "last_name":self.last_name, "phone_number": self.phone_number,
                "rank":self.rank}

    def __str__(self):
        # return (f"id:{self._id}\n"
        return (f""
                f"first name: {self.first_name}\n"
                f"last name: {self.last_name}\n"
                f"phone number: {self.phone_number}\n"
                f"rank: {self.rank}")