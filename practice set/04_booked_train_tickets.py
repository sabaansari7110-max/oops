# Class train which has methods to book a tikets, "getStatus" and "getfare" information of train runnning under indian railways

0
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo= trainNo

    def book(self, fro, to):
        print(f"Tickets is booked in train no.:  {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no.: {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no.: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t= Train(135990)
t.book("Rampur", "Delhi")
t.getStatus()
t.getfare("Rampur", "Delhi")
