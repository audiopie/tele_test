from datetime import datetime

class Postamat:

    def __init__(self, id, address, is_automated, accept_cash, accept_card, **kwargs):

        # Mandatory attributes
        self.id = id
        self.address = address
        self.is_automated = is_automated
        self.accept_cash = accept_cash
        self.accept_card = accept_card

        # optional possible and read-only attributes
        self.name = kwargs.get("name")
        self.type = kwargs.get("type")
        self.address_struct = kwargs.get("address_struct")
        self.status_code = kwargs.get("status_code")
        self.status = kwargs.get("status")
        self.description = kwargs.get("description")
        self.accept_payments = kwargs.get("accept_payments")
        self.working_hours = kwargs.get("working_hours")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_address_struct(self):
        return self.address_struct

    def get_description(self):
        return self.description

    @property
    def get_working_hours(self):
        return self.working_hours

    def is_working(self):
        day_now = datetime.today().weekday()  # return a number of day Monday=0, Sunday=6
        time_now = datetime.today().strftime("%H:%M")
        time_open = self.get_working_hours[day_now].get("time_open")
        time_close = self.get_working_hours[day_now].get("time_close")

        if time_open and time_close:
            if time_open <= time_now <= time_close:
                return f'Now {time_now} Postamat is working'
            else:
                return f'Postamat is not working at this time {time_now}'



























