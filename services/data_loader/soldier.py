class Soldier:

    def __init__(self, _id, first_name, last_name, phone_number, rank):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    def to_dict(self):
        return {"_id":self._id, "first_name":self.first_name,
                "last_name":self.last_name, "phone_number": self.phone_number,
                "rank":self.rank}

    def __str__(self):
        return (f"id:{self._id}\n"
                f"first name: {self.first_name}\n"
                f"last name: {self.last_name}\n"
                f"phone number: {self.phone_number}\n"
                f"rank: {self.rank}")