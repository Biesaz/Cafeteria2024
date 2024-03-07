class Restaurant:           # represent the restaurant establishment.

    def __init__(self, name, address, phone_number, menu):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.menu = menu
        self.tables = []
        pass

    def add_table(self, table,):
        self.tables.append(table)

    def list_tables(self):
        for table in self.tables:
            print(table)

    def reserve_table(self, customer_name, party_size, reservation_time):
        available_tables = [table for table in self.tables if table.is_available()]
        if not available_tables:
            print("Sorry, no tables available.")
            return

        for table in available_tables:
            if table.capacity >= party_size:
                table.mark_unavailable()
                reservation = Reservation(customer_name, party_size, reservation_time, table.table_number)
                print(f"Reservation confirmed: {reservation}")
                return

        print("Sorry, no tables available that can accommodate your party size.")