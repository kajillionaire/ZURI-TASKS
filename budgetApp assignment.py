import time
budget={}
class Budget:

    def __init__(self, category):
        self.category = category
        if category in budget:
            pass
        else:
            self.account_balance= 0
            budget[self.category]= self.account_balance

    def deposit(self):
        print('=' * 5,f'DEPOSIT TO {self.category} BUDGET', '=' * 5)
        amount_to_deposit = int(input('enter amount to deposit:\n'))
        self.account_balance = float(amount_to_deposit)
        budget[self.category]= amount_to_deposit
        print('processing...')
        time.sleep(2)
        print('deposit successful')
        new_transaction()
 

    def withdraw(self):
        print('=' * 5,f'WITHDRAW FROM {self.category} BUDGET', '=' * 5) 
        withdrawal_amount = int(input('Enter amount to withdraw:\n'))
        if budget[self.category] >= withdrawal_amount:
            budget[self.category] -= withdrawal_amount
            print('processing...')
            time.sleep(2)
            print('withdrawal successful')
            new_transaction()
        else:
            print('processing...')
            time.sleep(2)
            print('insufficient funds, Transaction failed')
            new_transaction()

    
    def transfer(self,category_to_transfer):
        print('=' * 5,f'TRANSFER FROM {self.category} BUDGET', '=' * 5)
        transfer_amount = int(input('Enter amount to deposit:\n'))
        if budget[self.category] >= transfer_amount:
            budget[self.category]-= transfer_amount
            if category_to_transfer in budget: 
                budget[category_to_transfer]+= transfer_amount
                print('processing...')
                time.sleep(2)
                print('Transfer successful')
                new_transaction()
            else:
                budget[category_to_transfer] = transfer_amount
                print('processing...')
                time.sleep(2)
                print('Transfer successful...')
                new_transaction()
        else:
            print('processing...')
            time.sleep(2)
            print('Insufficient funds, Transaction failed')
            new_transaction()


    def check_Balance(self):
        print('=' * 5,f'CHECK {self.category} BALANCE', '=' * 5)
        print("#",budget[self.category],".00")
        new_transaction()



def food_():
    print('=' * 5, 'FOOD-BUDGET', '=' * 5)
    food = Budget('food')
    food_Option= input('''You've the following options
    1. deposit
    2. withdraw
    3. transfer
    4. check balance \n ''')
    if food_Option == '1':

        food.deposit()
    elif food_Option == '2':
        food.withdraw()
    elif food_Option== '3':
        category_TO_transfer= input('''which category would you like to transfer to?
        1.clothing
        2.Entertainment \n''')
        if category_TO_transfer == '1':
            food.transfer('clothing')
        elif category_TO_transfer == '2':
            food.transfer('Entertainment')
        else:
            print('invalid option')
    elif food_Option == '4':
        food.check_Balance()
    else:
        print('invalid option selected')
        homepage()

def clothing_():
    print('=' * 5, 'CLOTHING-BUDGET', '=' * 5)
    clothing = Budget('clothing')
    clothing_Option= input('''You've the following options
    1. deposit
    2. withdraw
    3. transfer
    4. check balance \n ''')
    if clothing_Option == '1':
        clothing.deposit()
    elif clothing_Option == '2':
        clothing.withdraw()
    elif clothing_Option== '3':
        category_TO_transfer= input('''which category would you like to transfer to?
        1.food
        2.Entertainment \n''')
        if category_TO_transfer == '1':
            clothing.transfer('food')
        elif category_TO_transfer == '2':
            clothing.transfer('Entertainment')
        else:
            print('invalid option')
    elif clothing_Option == '4':
        clothing.check_Balance()
    else:
        print('invalid option selected')
        homepage()


def Entertainment_():
    print('=' * 5, 'ENTERTAINMENT-BUDGET', '=' * 5)
    Entertainment = Budget('Entertainment')
    Entertainment_Option= input('''You've the following options
    1. deposit
    2. withdraw
    3. transfer
    4. check balance \n ''')
    if Entertainment_Option == '1':
        Entertainment.deposit()
    elif Entertainment_Option == '2':
        Entertainment.withdraw()
    elif Entertainment_Option== '3':
        category_TO_transfer= input('''which category would you like to transfer to?
        1.food
        2.clothing \n''')
        if category_TO_transfer == '1':
            Entertainment.transfer('food')
        elif category_TO_transfer == '2':
            Entertainment.transfer('clothing')
        else:
            print('invalid option')
    elif Entertainment_Option == '4':
        Entertainment.check_Balance()
    else:
        print('invalid option selected')        
        homepage()

import sys
def homepage():
    print('=' * 5, 'WELCOME TO EFFs-BUDGET', '=' * 5 )
    select_option= input('''What would you like to budget for?
    1. Food
    2. Clothing
    3. Entertainment
    4. Exit \n''')
    if select_option == '1':
        time.sleep(2)
        food_()
    elif select_option == '2':
        time.sleep(2)
        clothing_()
    elif select_option== '3' :
        time.sleep(2)
        Entertainment_()
    elif select_option == '4':
        print('Exiting...')
        time.sleep(2)
        sys.exit()
    else:
        print('Invalid Option')
        time.sleep(2)
        homepage()

def new_transaction():
    new_T= input('''Would you like to make another transaction?
    1. yes
    2. no \n''')
    if new_T == '1':
        homepage()
    elif new_T == '2':
        exit()
    else:
        print('Invalid option selected')
        new_transaction()


homepage()   