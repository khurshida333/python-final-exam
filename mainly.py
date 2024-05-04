from user import Saving,Bank,Admin
from random import randint

sonali_bank=Bank("sonali bank limited")
kamal = Saving("Kamal", "kamal@gmail.com", "64274", "Dhaka", 80, sonali_bank)
jamal = Saving("Jamal", "jamal81@gmail.com", "72538", "Khulna", 81, sonali_bank)
tomal = Saving("Tomal", "tomal@gmail.com", "83526", "Kustia", 82, sonali_bank)

sonali_bank.add_account(kamal)
sonali_bank.add_account(jamal)
sonali_bank.add_account(tomal)

def saving_user_entry():
 
    name=input("Enter Your Name: ")
    email=input("Enter Your Email: ")
    nid=input("Enter Your Nid: ")
    address=input("Enter Your Address: ")
    ac_num=randint(100,200)
    savingAC=Saving(name,email,nid,address,ac_num,sonali_bank)
    sonali_bank.add_account(savingAC)

    while True:  
        print(f"Welcome {savingAC.name} . your saving account number is {ac_num}!!")
        print("1.Available Balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.see your Transaction History")
        print("5.see available accounts")
        print("6.Transfer Money")
        print("7.Take a loan")
        print("8.see your loan count")
        print("9.Exit")
 

        choice=int(input("Enter Your Choice: "))

        if choice==1:
            print(f"your current bank balance is {savingAC.bank_balance()}")
        elif choice==2:
            amount=int(input("Enter Your amount: "))
            savingAC.deposit(amount)
        elif choice==3:
            amount=int(input("Enter Your amount: "))
            savingAC.withdraw(amount)
        elif choice==4:
            sonali_bank.print_transection_history(ac_num)
        elif choice==5:
            sonali_bank.print_accounts()
        elif choice==6:
            frnd_ac_num=int(input("Enter Your friend account number : "))
            amount=int(input("Enter how much you wanna transfer : "))
            savingAC.transfer(frnd_ac_num,amount)
        elif choice==7:
            take_a_loan=int(input("Enter your loan amount : "))
            savingAC.take_a_loan(take_a_loan)
        elif choice==8:
            print(sonali_bank.loan_count[ac_num])
        elif choice==9:
            break
        else:
            print("Invalid Input.")

def current_user_entry():
 
    name=input("Enter Your Name: ")
    email=input("Enter Your Email: ")
    nid=input("Enter Your Nid: ")
    address=input("Enter Your Address: ")
    ac_num=randint(200,300) 
    savingAC=Saving(name,email,nid,address,ac_num,sonali_bank)
    sonali_bank.add_account(savingAC)

    while True:  
        print(f"Welcome {savingAC.name} . your current account number is {ac_num}!!")
        print("1.Available Balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.see your Transaction History")
        print("5.see available accounts")
        print("6.Transfer Money")
        print("7.Exit")
 

        choice=int(input("Enter Your Choice: "))

        if choice==1:
            print(f"your current bank balance is {savingAC.bank_balance()}")
        elif choice==2:
            amount=int(input("Enter Your amount: "))
            savingAC.deposit(amount)
        elif choice==3:
            amount=int(input("Enter Your amount: "))
            savingAC.withdraw(amount)
        elif choice==4:
            print(sonali_bank.transections[ac_num])
        elif choice==5:
            sonali_bank.print_accounts()
        elif choice==6:
            frnd_ac_num=int(input("Enter Your friend account number : "))
            amount=int(input("Enter how much you wanna transfer : "))
            savingAC.transfer(frnd_ac_num,amount)
        elif choice==7:
            break
        else:
            print("Invalid Input.")

def admin_entry():
    
    name=input("Enter Your Name: ")
    email=input("Enter Your Email: ")
    phone=input("Enter Your Phone: ")
    address=input("Enter Your Address: ")
    ac_num=randint(300,400)
    admin=Admin(name,phone,email,address,ac_num,sonali_bank)
    sonali_bank.add_account(admin)

    while True:  
        print(f"Welcome {admin.name} . your Admin account number is {ac_num}!!")
        print("1.see total bank balance")
        print("2.see available accounts")
        print("3.delete user")
        print("4.off loan feature")
        print("5.on loan feature")
        print("6.see total loan amount")
        print("7.Exit")


        choice=int(input("Enter Your Choice: "))


        if choice==1:
            print(sonali_bank.total_balance)
        elif choice==2:
            sonali_bank.print_accounts()
        elif choice==3:
            ac_num=int(input("Enter her account number : "))
            admin.delete_user(ac_num)
        elif choice==4:
            if sonali_bank.loan==True:
                sonali_bank.loan=False
                print("loan feature of this bank is off !!")
            else:
                print("loan feature is already off")
        elif choice==5:
            if sonali_bank.loan==False:
                sonali_bank.loan=True
                print("loan feature of this bank is on !!")
            else:
                print("loan feature is already on")
        elif choice==6:
            print(sonali_bank.total_loan_amount)
        elif choice==7:
            break
        else:
            print("Invalid Input.")


while True:
    print("---Welcome to sonali Bank Limited---")
    print("1.User")
    print("2.Admin")
    print("3.Exit")


    choice=int(input("Enter Your Choice: "))
    if choice==1:
        print("Chose your account type-->")
        print("1.Saving acoount")
        print("2.Current account")
        choice1=int(input("Enter Your Choice: "))
        if choice1==1:
            saving_user_entry()
        elif choice1==2:
            pass
        else:
            print("plz, input option 1 or 2")
    elif choice==2:
        admin_entry()
    elif choice==3:
        break
    else:
        print("Invalid Input!!")
