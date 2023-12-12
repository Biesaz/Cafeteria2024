class Restaurant:           # represent the restaurant establishment.

    def __init__(self, name, address, phone_number, menu):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.menu = menu
        pass

#     a. add_table() to add new tables to the restaurant's table list.
#     b. list_tables() to display a list of all available tables.
#     c. reserve_table() to accept a reservation request, checking 
# availability and updating the Table and Reservation objects accordingly.

    
class Table:                # represent individual tables in the restaurant.
    def __init__(self, table_number, capacity, availability):
        self.table_number = table_number
        self.capacity = capacity
        self.availability = availability
    pass

#     a. is_available() to check if the table is available for a particular reservation time.
#     b. mark_available() to set the table's availability to true.
#     c. mark_unavailable() to set the table's availability to false.

class Reservation:          # represent individual customer reservations
    def __init__(self, customer_name, party_size, reservation_time, table_id):
        self.customer_name = customer_name
        self.party_size = party_size
        self.reservation_time = reservation_time
        self.table_id = table_id

#     a. calculate_total() to calculate the total cost of the reservation based on the menu items ordered.
#     b. print_reservation() to display a detailed summary of the reservation details.

#     Create a user interface (UI) using the console module to facilitate user interaction with the reservation system.
        