class TipModel:
    def __init__(self, bill_amount = 0, tip_percent = 0):
        self.__bill_amount = bill_amount
        self.__tip_percent = tip_percent


    # Creates a getter property called "bill_amount"
    # Use Case: print(obj_name.bill_amount)
    @property
    def bill_amount(self):
        return self.__bill_amount


    @property
    def tip_percent(self):
        return self.__tip_percent

    # this creates an attributeless property
    # use this to prevent stale attributes for calculated
    # values.
    @property
    def tip_amount(self):
        return self.__bill_amount * self.__tip_percent

    # creates a setter property for the related attribute.
    # Use Case: obj_name.bill_amount = 24.00
    @bill_amount.setter
    def bill_amount(self, value):
        if value < 0:
            raise ValueError("Error: \"bill amount\" must be positive.")
        else:
            self.__bill_amount = value
    

    @tip_percent.setter
    def tip_percent(self, value):
        if value < 0:
            raise ValueError("Error: \"tip_percent\" must be positive.")
        else:
            self.__tip_percent = value / 100


    def __str__(self):
        return f"Bill: ${self.bill_amount}, {self.tip_percent * 100}% tip = {self.tip_amount}"

    
        
    