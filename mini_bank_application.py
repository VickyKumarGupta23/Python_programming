class customer :
    '''This class developed by Vicky and discuss bank operation '''
    bankname = 'Durga_Bank'
    def __init__(self,name,balance = 0.0):
        self.name=name
        self.balance=balance

    def deposite(self,amount):
        self.balance = self.balance + amount
        print("After deposite the balance of the account is:__",self.balance)

    def withdrawl(self,amount):
        if amount > self.balance:
            print("Insufficent balance so you can not make further operation please enter less amount or check your balance")

        else:          
            self.balance = self.balance - amount

            print("After withdrawl balance is:__",self.balance)


print("WelCome to >>",customer.bankname)
name = input("Enter your name:")

c = customer(name)
while True:
    print('d-Deposite\n w-withdrwal\n e-exit')
    option = input("chose your option")
    if option.lower() == 'd':
        amount = float(input("Enter the amount that you want to deposite"))
        c.deposite(amount)

    elif option.lower() == 'w':
        amount = float(input("Enter the amount that you want ot withdraw"))
        c.withdrawl(amount)

    elif option.lower() == 'e':
        print("Thank you for banking")
        break
    else:
        print("choose valid option")        