import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books a hotel by changing its availability from yes to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the Hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class Conformation:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
               Thank you for your reservation!
               Here are your booking data:
               Name: {self.customer_name}
               Hotel name: {self.hotel.name}
               """
        return content


print(df)
hotel_ID = input("Enter the id of the Hotel")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = Conformation(customer_name=name, hotel_object=hotel)
    reservation_ticket.generate()
else:
    print("Hotel is not free")

