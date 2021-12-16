class Students:
    first_name = None
    last_name = None
    phone_number = None
    address = None

    def __init__(self, first_name, last_name, phone_number, address):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_phone_number(phone_number)
        self.set_address(address)

    def set_first_name(self, first_name):
        #    if isinstance(last_name, str):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        #    if isinstance(last_name, str):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def set_phone_number(self, phone_number):
        #    if isinstance(phone_number, int):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address
