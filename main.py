import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")

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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, csv):
        card_data = {
            "number": self.number,
            "expiration": expiration,
            "holder": holder,
            "csv": csv
        }

        if card_data in df_cards:
            return True
        else:
            return False



print(df)
hotel_ID = input("Enter the id of the Hotel")
hotel = Hotel(hotel_ID)
if hotel.available():
    credit_card = CreditCard(number="123456")
    if credit_card.validate(expiration="12/26",
                             holder="John Doh", csv="123"):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = Conformation(customer_name=name, hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print("There was a problem with your payment!")
else:
    print("Hotel is not free")

