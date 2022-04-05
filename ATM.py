import sys

class ATM:

    withdrawal_limit = 10000
    balance = 50000

    def __init__(self):
        print('**** Welcome ****')

    def Balance_inquiry(self):
        print(f'Balance is : {self.balance}')
    
    def withdrawal(self):
        amount = int(input('Enter the amount to withdraw: '))  
        if(amount %100 ==0 and amount<= ATM.withdrawal_limit and amount < ATM.balance):
            print('Please collect your Cash')
            ATM.balance -= amount
        else:
            print('Invalid amount. Please enter valid amount')
    
    
    def fast_cash(self):
        print("""
        Please select the option:
        1. 1000
        2. 2000
        3. 5000
        4. 10000
        """)
        op = int(input('Please enter the option for withdrawal: '))
        if (op == 1 and ATM.withdrawal_limit > 1000 ):
            print('Please collect your cash')
        elif(op == 2 and ATM.withdrawal_limit > 2000):
            print('Please collect your cash')
        elif (op == 3 and ATM.withdrawal_limit > 1000 ):
            print('Please collect your cash')
        elif (op == 4 and ATM.withdrawal_limit > 1000 ):
            print('Please collect your cash')
        else:
            print('Select valid option')
    
    def menu_option():
        print("""Please select operation:
                1. Balance Inquiry
                2. withdrawal
                3. Fast_Cash
                4. Exit

                """)




atm = ATM()

while True: 
    op = int(input('Select the operation : '))
    if op < 0 or op > 4:
        print("select valid option")
    elif(op == 1):
        atm.Balance_inquiry()
    elif(op == 2):
        atm.withdrawal()
    elif(op == 3):
        atm.fast_cash()
    elif(op == 4):
        sys.exit()
   
 





