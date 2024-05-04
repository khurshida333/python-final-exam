from abc import ABC
from datetime import datetime

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # accounts = { [101] : account_obj }
        self.total_balance=0
        self.custom_balance={}
        self.loan_count={}
        self.loan=True
        self.total_loan_amount=0

    def add_account(self, ac_obj):
        self.accounts[ac_obj.ac_num] = ac_obj
        self.custom_balance[ac_obj.ac_num]=0
        self.accounts[ac_obj.ac_num].transactions = []
        self.loan_count[ac_obj.ac_num]=0

    def print_accounts(self):
        for ac_obj in self.accounts.values():
            print(f"user_name-->balance")
            print(f"{ac_obj.name}-->{self.custom_balance[ac_obj.ac_num]}")
    def total_bank_balance(self):
        return self.total_balance

    def print_transection_history(self,ac_num):
        print(f"Transaction History of : {self.accounts[ac_num].name}")
        for transaction in self.accounts[ac_num].transactions:
            print(f"    Date & Time : {transaction[0]}, Type: {transaction[1]}, Amount: {transaction[2]}")
            
class User(ABC):
    def __init__(self, name, email, nid, address, ac_num, bank):
        self.name = name
        self.email = email
        self.nid = nid
        self.address = address
        self.ac_num = ac_num
        self.bank = bank
class Saving(User):
    def __init__(self, name, email, nid, address, ac_num, bank):
        super().__init__(name, email, nid, address, ac_num, bank)

    def bank_balance(self):
            return self.bank.custom_balance[self.ac_num] 

    def deposit(self, amount):
        self.bank.custom_balance[self.ac_num] += amount
        self.bank.total_balance += amount
        self.transactions.append((datetime.now(), f"Withdrawn ", amount))
        print(f"Your {amount} taka deposited successfully!")
        print(f"Now your current balance is {self.bank.custom_balance[self.ac_num]}.")

    def withdraw(self, amount):
        if self.bank.custom_balance[self.ac_num] >= amount:
            if amount < self.bank.total_balance:
                self.bank.custom_balance[self.ac_num] -= amount
                self.bank.total_balance -= amount
                self.transactions.append((datetime.now(), f"Deposited ", amount))
                print(f"Your {amount} taka withdrawn successfully!")
                print(f"Now your current balance is {self.bank.custom_balance[self.ac_num]}.")
            else:
                print("-||- This bank is bankrupt -|| -")
        else:
            print("Insufficient funds.")

    def transfer(self, frnd_ac_num, amount):
        if frnd_ac_num in self.bank.accounts.keys():
            if self.bank.custom_balance[self.ac_num] >= amount:
                self.bank.custom_balance[self.ac_num] -= amount
                self.bank.custom_balance[frnd_ac_num] += amount
                self.transactions.append((datetime.now(), f"Transfer to {self.ac_num} ", amount))
                self.bank.accounts[frnd_ac_num].transactions.append((datetime.now(), f"Transfer from {self.ac_num} ", amount))
                print(f"Your {amount} taka transferred to your friend's account successfully!")
                print(f"Now your current balance is {self.bank.custom_balance[self.ac_num]}.")
            else:
                print("Insufficient funds.")
        else:
            print("Your friend's account number not found.")
    def take_a_loan(self,amount):
        if self.bank.loan_count[self.ac_num] < 2: 
            if self.bank.loan==True:
                if self.bank.total_balance > amount:
                    self.bank.loan_count[self.ac_num] += 1
                    self.bank.total_balance -= amount
                    self.bank.custom_balance[self.ac_num] += amount
                    self.bank.total_loan_amount += amount
                    self.transactions.append((datetime.now(), f"Taken a loan of ", amount))
                    print(f"congrats!! you have taken a loan of {amount}.")
                else:
                    print("-||-loan amount in too much-||-") # when i tried to take loan for 3rd time then 
            else:                                            # this line was printed
                print("-||-loan feature is off-||-")
        else:
            print("You can't take any more loan.")
           

class Admin(User,Bank):
    def __init__(self, name, email, nid, address, ac_num, bank):
        super().__init__(name, email, nid, address, ac_num, bank)


    def total_bank_balance(self):
        self.bank.total_bank_balance().total_balance

    def delete_user(self, ac_num):
        if ac_num in self.bank.accounts:
            del self.bank.accounts[ac_num]
            del self.bank.custom_balance[ac_num]
            self.bank.total_balance -= self.bank.custom_balance[self.ac_num] 
            print(f"User with account number {ac_num} has been deleted.")
        else:
            print("User not found.")

