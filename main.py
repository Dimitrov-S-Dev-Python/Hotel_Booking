import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

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

    def __init__(self, customer_name, hotel):
        pass

    def generate(self):
        pass


print(df)
hotel_ID = input("Enter the id of the Hotel")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = Conformation(hotel)
    reservation_ticket.generate()
else:
    print("Hotel is not free")

