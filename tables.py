class Tables:                # represent individual tables in the restaurant.
    def __init__(self, table_number, capacity, availability):
        self.table_number = table_number
        self.capacity = capacity
        self.availability = availability
    pass

    def is_available(self, reservation_time):
        return self.availability and not self.has_reservation(reservation_time)

    def mark_available(self):
        self.availability = True

    def mark_unavailable(self):
        self.availability = False

    def has_reservation(self, reservation_time):
        for reservation in restaurant.reservations:
            if reservation.table_id == self.table_number and reservation.reservation_time == reservation_time:
                return True
        return False