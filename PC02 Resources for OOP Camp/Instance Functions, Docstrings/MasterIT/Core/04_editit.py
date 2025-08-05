# Edit the add_date and show_dates instance functions
# - add_date should add the parameter date to the dates list
# - show_dates should output every date in the dates list to the console
class Calendar:
    def __init__(self):
        self.dates = []

    def add_date(self, date: str):
        pass

    def show_dates(self):
        pass


important_dates = Calendar()
important_dates.add_date("01/01/1970")
important_dates.add_date("01/01/1971")
important_dates.add_date("10/02/1973")
important_dates.show_dates()
