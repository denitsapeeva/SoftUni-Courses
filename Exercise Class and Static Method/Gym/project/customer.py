class Customer:
    customer_id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        Customer.customer_id +=1


    @staticmethod
    def get_next_id():
        return Customer.customer_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
