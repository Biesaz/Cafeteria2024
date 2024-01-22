# ORM 2 užduotis  DonatasNoreika edited this page on Mar 3, 2021 · 4 revisions
# https://github.com/DonatasNoreika/Python-pamokos/wiki/ORM-2-u%C5%BEduotis

# Asmenys, sąskaitos, bankai
# Padaryti programą, kurį leistų įvesti asmenis, bankus, asmenims priskirti sąskaitas bankuose.

# Asmuo turi vardą, pavardę, asmens kodą, tel. numerį.
# Bankas turi pavadinimą, adresą, banko kodą, SWIFT kodą
# Sąskaita turi numerį, balansą, priskirtą asmenį ir banką
# Asmuo gali turėti daug sąskaitų tame pačiame arba skirtinguose bankuose
### Padaryti duomenų bazės schemą (galima ją parodyti dėstytojui).
# Sukurti programą su UI konsolėje, kuri leistų įvesti asmenis, bankus, sąskaitas. 
# Leistų vartotojui peržiūrėti savo sąskaitas ir jų informaciją, pridėti arba nuimti iš jų pinigų. 
# Taip pat leistų bendrai peržiūrėti visus bankus, vartotojus, sąskaitas ir jų informaciją.

from Cafeteria2024.restoran import engine, Asmuo, Bankas, Saskaita
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("1 - įveskite vartotoją\n2 - įveskite banką\n3 - įveskite sąskaitą\n4 - įveskite pajamas/išlaidas\n6 - peržiūrėti vartotojus\n7 - peržiūrėti bankus\n8 - peržiūrėti sąskaitas\n9 - išeiti iš programos: \n"))
    if pasirinkimas == 1:
        vardas = input("Įveskite vardą: ")
        pavarde = input("Įveskite pavardę: ")
        asmens_kodas = int(input("Įveskite asmens kodą: "))
        el_pastas = input("Įveskite el. pašto adresą: ")
        asmuo = Asmuo(vardas=vardas, pavarde=pavarde, asmens_kodas=asmens_kodas, el_pastas=el_pastas)
        session.add(asmuo)
        session.commit()
    if pasirinkimas == 2:
        pavadinimas = input("Įveskite banko pavadinimą: ")
        adresas = input("Įveskite adresą: ")
        banko_kodas = input("Įveskite banko kodą: ")
        swift_kodas = input("Įveskite SWIFT kodą: ")
        bankas = Bankas(pavadinimas=pavadinimas, adresas=adresas, banko_kodas=banko_kodas, swift_kodas=swift_kodas)
        session.add(bankas)
        session.commit()
    if pasirinkimas == 3:
        numeris = input("Įveskite sąskaitos numerį: ")
        balansas = 0
        vartotojai = session.query(Asmuo).all()
        for vartotojas in vartotojai:
            print(vartotojas)
        vartotojo_id = int(input("Pasirinkite vartotojo ID: "))
        bankai = session.query(Bankas).all()
        for vienas in bankai:
            print(vienas)
        banko_id = int(input("Pasirinkite banko ID: "))
        saskaita = Saskaita(numeris=numeris, balansas=balansas, asmuo_id=vartotojo_id, bankas_id=banko_id)
        session.add(saskaita)
        session.commit()
    if pasirinkimas == 4:
        saskaitos = session.query(Saskaita).all()
        for viena in saskaitos:
            print(viena)
        saskaitos_id = int(input("Pasirinkite sąskaitos ID: "))
        pasirinkta_saskaita = session.query(Saskaita).get(saskaitos_id)
        irasas = float(input("Įveskite pajamas/išlaidas (su -): "))
        pasirinkta_saskaita.balansas += irasas
        session.commit()
    if pasirinkimas == 6:
        vartotojai = session.query(Asmuo).all()
        for vartotojas in vartotojai:
            print(vartotojas)
    if pasirinkimas == 7:
        bankai = session.query(Bankas).all()
        for vienas in bankai:
            print(vienas)
    if pasirinkimas == 8:
        saskaitos = session.query(Saskaita).all()
        for viena in saskaitos:
            print(viena)
    if pasirinkimas == 9:
        print("Programa baigta")
        break

###################################################################
class Restaurant:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.menu = {}
        self.tables = []

    def add_table(self, table_number, capacity):
        table = Table(table_number, capacity)
        self.tables.append(table)

    def list_tables(self):
        print("List of available tables:")
        for table in self.tables:
            if table.is_available():
                print(f"Table Number: {table.table_number}")
                print(f"Capacity: {table.capacity}")

    def reserve_table(self, customer_name, party_size, reservation_time):
        # Check if a suitable table is available
        available_tables = [table for table in self.tables if table.is_available() and table.capacity >= party_size]

        if not available_tables:
            print("No suitable tables available.")
            return

        # Select the first available table
        table = available_tables[0]
        table.mark_unavailable()

        # Create a reservation object
        reservation = Reservation(customer_name, party_size, reservation_time, table.table_number)
        self.reservations.append(reservation)

        print(f"Reservation successful! Table {table.table_number} is reserved for {customer_name}.")

class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.availability = True

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

class Reservation:
    def __init__(self, customer_name, party_size, reservation_time, table_id):
        self.customer_name = customer_name
        self.party_size = party_size
        self.reservation_time = reservation_time
        self.table_id = table_id

    def calculate_total(self):
        total = 0
        for menu_item, quantity in self.order_items.items():
            total += menu_item.price * quantity
        return total

    def print_reservation(self):
        print("Reservation details:")
        print(f"Customer Name: {self.customer_name}")
        print(f"Party Size: {self.party_size}")
        print(f"Reservation Time: {self.reservation_time}")
        print(f"Table Number: {self.table_id}")
        print("Order Items:")
        for menu_item, quantity in self.order_items.items():
            print(f"{menu_item.name} - {quantity}")

if __name__ == "__main__":
    restaurant = Restaurant("Cafeteria", "123 Main St", "555-555-5555")
    restaurant.add_table(1, 2)
    restaurant.add_table(2, 4)

    # User interface
    while True:
        print("Choose an action:")
        print("1. View restaurant details and menu")
        print("2. Browse available tables and make reservations")
        print("3. View your existing reservations")
        print("4. Manage your reservation details")
        print("5. Quit")

        option = int(input("Enter your choice: "))

        if option == 1:
            restaurant.print_details()
            restaurant.print_menu()
        elif option == 2:
            table_number = int(input("Enter the desired table number: "))
            party_size = int(input("Enter the number of guests: "))
            reservation_time = input("Enter the reservation time: ") # TODO: validate input
            restaurant.reserve_table(table_number, party_size, reservation_time)
        elif option == 3:
            # TODO: list reservations
            pass
        elif option == 4:
            # TODO: manage reservations
            if option == 4:
                print("Manage your reservation details:")
                print("1. View reservation details")
                print("2. Modify reservation")
                print("3. Cancel reservation")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    # TODO: view reservation details
                    pass
                elif choice == 2:
                    # TODO: modify reservation
                    pass
                elif choice == 3:
                    # TODO: cancel reservation
                    pass