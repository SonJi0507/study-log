# --- clinet ---
class You:
    def __init__(self):
        print("You:: Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You:: Denim shirt is Mine")
        else :
            print("You:: I should earn more")


# --- subject ---
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


# --- real subject ---
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account
    
    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return True
    
    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else :
            print("Bank:: Sorry, not enough funds!")
            return False


# --- Proxy ---
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()


you = You()
you.make_payment()

"""
You:: Lets buy the Denim shirt
Proxy:: Punch in Card Number: 1234
Bank:: Checking if Account 1234 has enough funds
Bank:: Paying the merchant
"""

"""
You:: Lets buy the Denim shirt
Proxy:: Punch in Card Number 1234
Bank:: Checking if Account 1234 has enough funds
Bank:: Sorry, not enough funds!
You:: I should earn more
"""