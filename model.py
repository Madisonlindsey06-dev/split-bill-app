class TipModel:
    def __init__(self, bill_amount=0, tip_percent=0, num_people=1):
        self.__bill_amount = bill_amount
        self.__tip_percent = tip_percent
        self.__num_people = num_people  # new attribute

    # --- Existing properties ---
    @property
    def bill_amount(self):
        return self.__bill_amount

    @property
    def tip_percent(self):
        return self.__tip_percent

    @property
    def tip_amount(self):
        return self.__bill_amount * self.__tip_percent

    # --- New num_people property ---
    @property
    def num_people(self):
        return self.__num_people

    @num_people.setter
    def num_people(self, value):
        if value < 1:
            raise ValueError('Error: "num_people" must be at least 1.')
        self.__num_people = value

    # --- Existing setters ---
    @bill_amount.setter
    def bill_amount(self, value):
        if value < 0:
            raise ValueError('Error: "bill amount" must be positive.')
        self.__bill_amount = value

    @tip_percent.setter
    def tip_percent(self, value):
        if value < 0:
            raise ValueError('Error: "tip_percent" must be positive.')
        self.__tip_percent = value / 100

    # --- New calculated property: total_per_person ---
    @property
    def total_per_person(self):
        return (self.bill_amount + self.tip_amount) / self.num_people

    # --- Updated string representation ---
    def __str__(self):
        return (f"Bill: ${self.bill_amount}, "
                f"{self.tip_percent * 100}% tip = ${self.tip_amount:.2f}, "
                f"split among {self.num_people} people = ${self.total_per_person:.2f} per person")
