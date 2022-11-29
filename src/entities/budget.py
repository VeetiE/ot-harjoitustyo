class Budget:
    def __init__(self, name, user, amount, beginning_date, ending_date, current_date):
        self.amount = amount
        self.name = name
        self.user = user
        self.beginning_date = beginning_date
        self.ending_date = ending_date
        self.current_date = current_date
