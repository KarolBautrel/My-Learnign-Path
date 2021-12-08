import datetime as dt


class Trip:

    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    @classmethod
    def publis_offer(cls, trips):
        list_of_errors = []
        for i in trips:
            try:
                i.check_data()
            except ValueError as e:
                list_of_errors.append("{}:{}".format(i.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}".format((i.symbol, str(e))))
        else:
            print("The offer will be published")


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))]


try:
    print("Starting checking trips")
    Trip.publis_offer(trips)
except Exception as e:
    print("Terrible {}".format(e))
