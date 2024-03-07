from typing import Union

class Reservation:
    def __init__(self, customer_name, party_size, reservation_time, table_id):
        self.customer_name = customer_name
        self.party_size = party_size
        self.reservation_time = reservation_time
        self.table_id = table_id
        

    def new_reservation() -> str:
        while True:
            user_answer = input("Do you want to make a new reservation?(Yes/No): ").strip().lower()
            if user_answer != "yes" and user_answer != "no":
                print("You must type yes or no")
                continue
            else:
                return user_answer
            

    def going_to_eat_now() -> str:
        while True:
            user_answer = input("Are you going to eat now?(Yes/No): ").strip().lower()
            if user_answer != "yes" and user_answer != "no":
                print("You must type yes or no")
                continue
            else:
                return user_answer
            
    def reservation_info() -> Union[str, int]:
        name = input("Could you tell us your name? ").strip()
        table_type = get_valid_table_type()
        table_id = get_valid_table_id()
        user_answer = is_going_to_eat_now()
        
        return name, table_type, table_id