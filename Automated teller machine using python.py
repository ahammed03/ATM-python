# Define a class for Automated_Teller_Machine
class Automated_Teller_Machine:
    def __init__(self):
        self.account_number = 0
        self.name = ""
        self.place = ""
        self.atm_pin = 0
        self.atm_card_number = 0
        self.amount = 0
    
    # Method to create an account
    def create_account(self, acc_no, name, place, atm_no, atm_pin, amount):
        self.account_number = acc_no
        self.name = name
        self.place = place
        self.atm_pin = atm_pin
        self.atm_card_number = atm_no
        self.amount = amount 
        
    # Method to get input and verify ATM details
    def get_input(self):
        atm_no = int(input("Enter Your ATM number: "))
        for i in database:
            if i["atm_no"] == atm_no:
                atm_pin = int(input("Enter Your Pin: "))
                if i["atm_pin"] == atm_pin:
                    return i
        return False
    
    # Method to get account details
    def get_acc_details(self, db):
        print(f'\nAccount Number    :- {db["atm_no"]} \nName              :- {db["name"]} \nPlace             :- {db["place"]}')
        
    # Method to change ATM pin
    def change_atm_pin(self, acc_no, old_pin, new_pin):
        if self.account_number == acc_no and self.atm_pin == old_pin:
            self.atm_pin = new_pin 
            print("Your ATM Pin has been successfully changed")
        else:
            print("Please enter correct details") 
    
    # Method for balance enquiry
    def balance_enquiry(self, db):
        print(f'\n Your Account Balance: {db["amount"]}')  
    
    # Method for withdrawal
    def with_draw(self, atm_no, atm_pin):
        if self.atm_pin == atm_pin and self.atm_card_number == atm_no: 
            x = int(input("Enter Amount to withdraw: ")) 
            if x <= self.amount:
                print(f"Please collect the Cash: {x}")
                print(f'Your remaining balance: {x - self.amount}')
            elif x > self.amount:
                print("Insufficient Funds")

# Create an instance of Automated_Teller_Machine
obj = Automated_Teller_Machine()

# Define the database of accounts
global database
database = [
    {"acc_no": 0000, "name": "user1", "place": "place_1", "atm_no": 000, "atm_pin": 000, "amount": 120000},
    {"acc_no": 1111, "name": "user_2", "place": "place_2", "atm_no": 111, "atm_pin": 111, "amount": 450000}
]

# Display menu to the user
print('''\n Welcome to XYZ bank 
      
please select the options 

1 Account Information     2 Balance Enquiry
3 Change Pin              4 Withdraw 
5 Create Account          0 Cancel
''')

# Get user input
user_input = int(input(":-"))
l = [0, 1, 2, 3, 4, 5]

# Check user input and execute corresponding actions
if user_input not in l:
    print("Please choose a valid option")
elif user_input == 0:
    print("\nThank you for banking with us")
elif user_input == 1:
    db = obj.get_input()
    if db:
        obj.get_acc_details(db)
    else:
        print('''Invalid Details
        Please enter valid details''')
elif user_input == 2:
    db = obj.get_input()
    if db:
        obj.balance_enquiry(db)
    else:
        print("Invalid Details")
elif user_input == 3:
    db = obj.get_input()
    if db:
        new_pin = int(input("Enter Your New Pin: "))
        db["atm_pin"] = new_pin 
        print("Your new pin:", db["atm_pin"])
    else:
        print("Invalid Details")
elif user_input == 4:
    db = obj.get_input()
    if db:
        withdraw_amnt = int(input("Enter the Amount: "))
        if db["amount"] > withdraw_amnt:
            db["amount"] -= withdraw_amnt
            print("Your Transaction is processing")
            print("Please collect cash") 
        else:
            print("Insufficient Funds")
    else:
        print("Invalid Details")
elif user_input == 5:
    pass  # Placeholder for the "create account" functionality
